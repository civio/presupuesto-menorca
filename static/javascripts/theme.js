// Theme custom js methods
$(document).ready(function(){

  var addYearSelectorCustomLabels = function(){
    var str2024 = {
      'es': 'prorrogado',
      'ca': 'prorrogat',
    };

    $('.data-controllers .layout-slider .slider .slider-tick-label').each(function(){
      var val = $(this).html();
      if (val === '2024'){
        $(this).html(val + '<br/><small><i> ('+ str2024[ $('html').attr('lang') ] +')</i></small>');
      }
    });
  };

  addYearSelectorCustomLabels();
});
