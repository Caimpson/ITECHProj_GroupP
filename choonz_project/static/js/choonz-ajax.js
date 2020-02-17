$(document).ready(function(){
	$('#like_btn').click(function(){
		var categoryIdVar
		categoryIdVar = $(this).attr('data-categoryid');

		// url of get request
		// then parameters
		// then anonymous function to handle returned data
		$.get('/choonz/like_category/', {'category_id': categoryIdVar}, function(data){
			$('#like_count').html(data);
			$('#like_btn').hide();
		})
	})

	$('#search-input').keyup(function() {
		var query;
		query = $(this).val();

		$.get('/choonz/suggest/', {'suggestion': query}, function(data){
			$('#categories-listing').html(data);
		})
	})

	$('.choonz-page-add').click(function() {
		var categoryid = $(this).attr('data-categoryid');
		var title = $(this).attr('data-title');
		var url = $(this).attr('data-url');
		var clickedButton = $(this);

		$.get('/choonz/search_add_page/', {'category_id': categoryid, 'title': title, 'url': url}, function(data){
			$('#page-listing').html(data);
			clickedButton.hide();
		})

	})
	
})

