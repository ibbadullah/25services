$('li[class^="subswatch-"],li[class*=" subswatch-"]').click(function() {
	var selectedSwatch = $(this);
	var selectedSwatchName = selectedSwatch.data('tooltip');
	var selectedSwatchNumber = selectedSwatch.attr('class').match(/\d+/)[0];
	var selectedSwatchParent = selectedSwatch.closest('ul');
	var selectedSwatchParentOffset = selectedSwatchParent.css('top');
	var selectedColor = selectedSwatch.css('background-color');
	var selectedOffset = selectedSwatch.offset();
	var cardOffset = $('.card').offset();
	var rippleOriginTop = selectedOffset.top - cardOffset.top + (selectedSwatch.outerHeight() / 2);
	var rippleOriginLeft = selectedOffset.left - cardOffset.left + (selectedSwatch.outerWidth() / 2);
	var newParentOffset = -(((selectedSwatchNumber - 1) * 54) + 4);

	console.log(selectedSwatchNumber);
	console.log(newParentOffset);

	$('.color-picker .active').removeClass('active');
	selectedSwatchParent.css("top", newParentOffset);
	selectedSwatchParent.find('.centered').removeClass('centered');
	selectedSwatch.addClass('active centered');
	$('.ripple').css({
		left: rippleOriginLeft,
		top: rippleOriginTop,
		backgroundColor: selectedColor
	}).addClass('scaling');

	setTimeout(function() {
		$('body').css({
			backgroundColor: selectedColor
		});
		$('.color-name').empty().append(selectedSwatchName);
	}, 400);
	setTimeout(function() {
		$('.ripple').removeClass('scaling');
	}, 900);
})