<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>


$('#bike-modal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var bike = button.data('id') 
  var modal = $(this)
  modal.find('.modal-model').text(bike.model)
  modal.find('.modal-type').text(bike.type)
  modal.find('.modal-year').text(bike.year)
  modal.find('.modal-size').text(bike.size)
  modal.find('.modal-price').text(bike.price)

})

$('bike_detail').click(function(){
  var bikeid;
  bikeid = $(this).attr("data-id");
  $.get('bikeShop/bike/', {bike_id: bikeid}, function(data){
    $('#bike').html(data);
  });
});