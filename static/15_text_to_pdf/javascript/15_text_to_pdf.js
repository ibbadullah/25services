var content = document.getElementById('text'),
button = document.getElementById('button');

function generatePDF(){
  var doc = new jsPDF();

  doc.setFontSize(14);
  doc.text(20, 20, content.value);
  //doc.text(35, 25, "Paranyan loves jsPDF");
  //doc.addImage(imgData, 'JPEG', 15, 40, 180, 160);
  doc.save('my.pdf');
}

button.addEventListener('click', generatePDF);

$(document).ready(function(){
  $('#title').focus();
    $('#text').autosize();
});

