// Custom Code by Dante and some reference annotations on each function
// --------------------------------------------------------------------

function isLetter(s) {
  return s.match("^[a-zA-Z()]+$");
}

// By lov2dev.com
/*function capitalize(str) {
              return str.replace(/[a-z]/ig, function (letter) {
                return letter.toUpperCase();
              });
            }*/

// By lov2dev.com --------------
function titleCase(str) {
  return str.replace(/\w\S/i, function (t) {
    return t.toUpperCase();
  });
}

function sentenceCase(str) {
  return str.replace(/[a-z]/i, function (letter) {
    return letter.toUpperCase();
  });
}

// by lov2dev.com
function invertCase(str) {
  var output = "";

  for (var i = 0; i < str.length; i++) {
    var ch = str[i];

    if (ch === ch.toUpperCase()) {
      output += ch.toLowerCase();
    } else {
      output += ch.toUpperCase();
    }
  }

  return output;
}

function textToLowercase() {
  jQuery("#input").val(jQuery("#input").val().toLowerCase());
}

function textToUpperCase() {
  jQuery("#input").val(jQuery("#input").val().toUpperCase());
}

function applyCase(textCase) {
  if (textCase == "lowercase") {
    textToLowercase();
  } else if (textCase == "uppercase") {
    textToUpperCase();
  } else if (textCase == "capitalize") {
    textToLowercase();
    let inputText = jQuery("#input");
    let lines = inputText.val().split("\n");

    inputText.val('')
    lines.forEach((line) => {
      let words = line.split(' ');
      let wordsCapitalized = [];
      words.forEach((word) => {
        word = word.toLowerCase();
        word = word.charAt(0).toUpperCase() + word.slice(1);
        wordsCapitalized.push(word);
      });
      inputText.val(inputText.val() + wordsCapitalized.join(" ") + '\n');
      words = [];
    });
  } else if (textCase == "sentence") {
    textToLowercase();
    let inputText = jQuery("#input").val();
    let sentences = inputText.match(/[^\.!\?]+[\.!\?]+["']?|\s*$|[^\r\n]+/g);

    let sentencesCapitalized = [];
    sentences.forEach((sentence) => {
      sentence = sentenceCase(sentence);
      sentencesCapitalized.push(sentence);
    });
    jQuery("#input").val(sentencesCapitalized.join(""));
    sentences = [];
  } else if (textCase == "invert") {
    jQuery("#input").val(invertCase(jQuery("#input").val()));
  }
}

// Global functions for tools
function copyToClipboard(idElement = 'output') {
  let copyText = document.getElementById(idElement);
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  document.execCommand("copy");

  let check = document.getElementById("check");
  check.classList.remove('none');
  setTimeout(() => {
    check.classList.add('none');
  }, 3000);
}

// Word count
function wordCount(idElement, maxLength = 100000) {
  var maxLength = maxLength;
  jQuery("#max-length-chars").text(maxLength);
  jQuery('textarea#' + idElement).attr("maxlength", maxLength);
  jQuery('textarea#' + idElement).keyup(function () {
    var textlen = jQuery(this).val().length;
    jQuery("#counting-chars").text(textlen);
  });
}

wordCount('input', 100000)