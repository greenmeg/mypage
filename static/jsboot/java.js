$(function() {
  $('a[@rel*=lightbox]').lightBox({
    overlayBgColor: '#FFF',
    overlayOpacity: 0.6,
    imageLoading: 'http://example.com/images/loading.gif',
    imageBtnClose: 'http://example.com/images/close.gif',
    imageBtnPrev: 'http://example.com/images/prev.gif',
    imageBtnNext: 'http://example.com/images/next.gif',
    containerResizeSpeed: 350,
    txtImage: 'Imagem',
    txtOf: 'de'
   });
});