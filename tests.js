function test() {

    var spans2 = document.querySelector(".transcription").children;

    //var spans = document.querySelector(".translation").children;
    var total = document.querySelector(".translation").children.length;

    for (var i=0; i<total; i++) {
        //var span = spans[i].getAttribute("phrase");
        var span = phrases_array[i];
        var l = spans2[i].childNodes.length;
        var text = "";
        for (var j=0;j < l;j++) {
            if (spans2[i].childNodes[j].nodeName==="SPAN") {
                text += spans2[i].childNodes[j].childNodes[1].nodeValue;
            } else if (spans2[i].childNodes[j].nodeName==="#text") {
                text += spans2[i].childNodes[j].nodeValue;
            }
        }
        //var span2 = spans2[i].innerText;

        if (span !== text) {

            console.log(i);
            console.log(span);
            console.log(text);
        }

    }
}

function proper_translation_markup() {
    var transcriptions = document.querySelector(".transcription").children;
    var translations = document.querySelector(".translation").children;

    var prev_offsettop = 0;
    var words_in_line = 0;
    //var translations_in_line = 0;
    var br_count = 0;
    //var index_for_translations = 0;
    var prev_offsettop_el_i = 0;
    var line = 1;
    var prev_tr_element = null;
    for (var i=0; i < transcriptions.length; i++) {
        var span_l = transcriptions[i].children.length;

        var spansonly = [].filter.call(translations[i].children, function(el) {
				return el.nodeName === "SPAN";
			});
        if (spansonly.length !== span_l) {
            console.log("error in line "+line+" "+i+" "+j);
            return;
        }

        for (var j=0; j<span_l; j++) {

            if (transcriptions[i].children[j].offsetTop > prev_offsettop) {
                if (spansonly[j].previousElementSibling !== null) {
                    if (spansonly[j].previousElementSibling.nodeName === "BR") {

                    }
                    else {
                        console.log("error in line "+line+" "+i+" "+j);
                        return;
                    }
                } else {
                    //предыдущий спан с меньшим offset top

                    if (translations[prev_offsettop_el_i].children.length ===0) {
                        console.log("error in line "+line+" "+i+" "+j);
                        return;
                    }
                    var lastind = translations[prev_offsettop_el_i].children.length-1;

                    if (translations[prev_offsettop_el_i].children[lastind].nodeName === "BR") {

                    }
                    else {
                        console.log("error in line "+line+" "+i+" "+j);
                        return;
                    }



                }

                words_in_line = 0;
                line++;
            }

            words_in_line++;

            //translations_in_line++;


            prev_offsettop = transcriptions[i].children[j].offsetTop;
            prev_offsettop_el_i = i;
            //prev_offsettop_el_j = j;


        }

    }


}

