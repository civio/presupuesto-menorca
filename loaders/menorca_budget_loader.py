# -*- coding: UTF-8 -*-
from budget_app.models import *
from budget_app.loaders import SimpleBudgetLoader
from decimal import *
import csv
import os
import re

class MenorcaBudgetLoader(SimpleBudgetLoader):

    # An artifact of the in2csv conversion of the original XLS files is a trailing '.0', which we remove here
    def clean(self, s):
        return s.split('.')[0]

    # We override this to allow a different classification per year
    def get_institutional_classification_path(self, path):
        return os.path.join(path, 'clasificacion_organica.csv')

    def parse_item(self, filename, line):
        # Programme codes have changed in 2015, due to new laws. Since the application expects a code-programme
        # mapping to be constant over time, we are forced to amend budget data prior to 2015.
        # See https://github.com/dcabo/presupuestos-aragon/wiki/La-clasificaci%C3%B3n-funcional-en-las-Entidades-Locales
        programme_mapping = {
            # old programme: new programme
            '13500': '13600',    # Servei Prevenció i Extinció d'Incendis i Salvament
            '15200': '15100',    # Disciplina urban., litoral, habitab. i act. clas.
            '16900': '92201',    # Servei de Cooperació i Assitència als Municipis
            '16920': '92202',    # Servei Insular d'Acollida d'Animals
            '17000': '15100',    # Ordenació Territorial
            '23000': '23100',    # Aga Direc. Insular atenció a persones i promoció aut. person
            '23010': '23101',    # AGA Dirc, Insular atenció dona, infància, joventut i immig.
            '23110': '23111',    # Supervisió i xarxa EMIF
            '23210': '23121',    # Política de gèner i igualtat
            '23220': '23122',    # Atenció a les drogodependències
            '23230': '23123',    # Servei insular de familia
            '23240': '23124',    # PROMOCIÓ DE LA SALUT
            '23250': '23125',    # Xrxa d'atenció a l'immigrant i nouvingut
            '23310': '23131',    # Suport social i comunitari
            '23320': '23132',    # Centres de dia per a persons amb discapacitat psiquiàtrica
            '23330': '23133',    # Residència gent gran i Centre de dia d'Alzheimer
            '23340': '23134',    # Promició i atenció gent gran, dependent, i envelliment actiu
            '23350': '23135',    # Residències i centre de dia persones discapacitat
            '31300': '31100',    # Promoció de la Salut
            '32300': '32600',    # Educació
            '34000': '92910',    # Esports
            '92930': '92230',    # Servei mancomunat de Prevenció de Riscos Laborals
            '41600': '41910',    # Caça
            '94550': '94300',    # Plans Insulars de Cooperació
        }

        # Some dirty lines in input data
        if line[0]=='':
            return None

        is_expense = (filename.find('gastos.csv')!=-1)
        is_actual = (filename.find('/ejecucion_')!=-1)
        if is_expense:
            # The functional codes have slightly different formats depending on the year
            year = re.search('municipio/(\d+)/', filename).group(1)
            if int(year) < 2015:
                # We got 4- functional codes as input, but the leading zero is lost sometimes.
                # And then make them 5- to match more recent codes.
                fc_code = self.clean(line[1]).rjust(4, '0').ljust(5, '0')
                # And amend the programme code if needed
                fc_code = programme_mapping.get(fc_code, fc_code)
            else:
                # We got 5- functional codes as input, but the leading zero is lost sometimes
                fc_code = self.clean(line[1]).rjust(5, '0')

            ec_code = self.clean(line[2])
            ic_code = self.clean(line[0]).rjust(3, '0')
            return {
                'is_expense': True,
                'is_actual': is_actual,
                'fc_code': fc_code,
                'ec_code': ec_code[:-4],        # First three digits (everything but last four)
                'ic_code': ic_code,
                'item_number': ec_code[-4:],    # Last four digits
                'description': line[3],
                'amount': self._parse_amount(line[10 if is_actual else 7])
            }

        else:
            ec_code = self.clean(line[0])
            return {
                'is_expense': False,
                'is_actual': is_actual,
                'ec_code': ec_code[:-2],        # First three digits
                'ic_code': '000',               # All income goes to the root node
                'item_number': ec_code[-2:],    # Last two digits
                'description': line[1],
                'amount': self._parse_amount(line[5 if is_actual else 2])
            }
