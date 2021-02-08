function test() {
    var res = [];
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
                if (spans2[i].childNodes[j].childNodes[1]===undefined) {
                     text += "";
                } else {
                    text += spans2[i].childNodes[j].childNodes[1].nodeValue;
                }


            } else if (spans2[i].childNodes[j].nodeName==="#text") {
                text += spans2[i].childNodes[j].nodeValue;
            }
        }
        //var span2 = spans2[i].innerText;
        //res.push(text);
        if (span !== text) {

            console.log(i);
            console.log(span);
            console.log(text);
        }

    }
    //console.log(JSON.stringify(res));
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

            //prev_offsettop_el_j = j;


        }
        if (span_l===0) {
            prev_offsettop = transcriptions[i].offsetTop;
        }


        prev_offsettop_el_i = i;

    }


}

function print_story() {
    var pure = function (phrase) {
        var str = phrase.trim();
        str = str.replace(/[^a-z ]/gi, '').toLowerCase();

        return str;

    }

    var get_rid_of_markup = function (span) {
        var l = span.childNodes.length;
        var text = "";
        for (var j=0;j < l;j++) {
            if (span.childNodes[j].nodeName==="SPAN") {
                if (span.childNodes[j].childNodes[1]===undefined) {
                     text += "";
                } else {
                    text += span.childNodes[j].childNodes[1].nodeValue;
                }


            } else if (span.childNodes[j].nodeName==="#text") {
                text += span.childNodes[j].nodeValue;
            }
        }
        return text;
    }
    console.log("start");
    var prev = [0,"0_0"];
    //var ind = 0;
    var real_text;
    var prev_middle_sended_index=1;
    var spans_what_we_see = document.querySelector(".transcription").children;
    var spans_raw = unblocked_html;

    for (var i = 0; i < story.length; i++) {
        if (story[i][2]===undefined) {
            prev = story[i];
            continue;
        } else if (i >0) {

            var p = story[i][1].split("_");
            var p2 = prev[1].split("_");
            /*if ((parseInt(p[1])+4)-story[i][0]!==1) {
                console.log((parseInt(p[1])+4)+"_"+story[i][0]);
            }*/
            if (p[1]-prev_middle_sended_index > 1) {
                console.log("increment "+i);
            }
            if (p[1]-p2[1] === 1) {
                if (pure(story[i][2]) === pure(prev[3]) && pure(story[i][3]) === pure(prev[4])) {
                    if (pure(story[i][3]) === pure(spans_raw["0_"+p[1]])) {

                    } else {
                        console.log("not equal raw text with what was sended: "+i+" "+p[1]+" "+spans_raw["0_"+p[1]]);
                    }

                    real_text = get_rid_of_markup(spans_what_we_see[p[1]]);
                    if (pure(real_text) === pure(story[i][3])) {

                    } else {
                        console.log("not equal real text with what was sended: "+i+" "+p[1]+" "+real_text);
                    }

                    if (pure(real_text) === pure(spans_raw["0_"+p[1]])) {

                    } else {
                        console.log("not equal real text with raw text:"+i+" "+p[1]+" "+real_text+" : "+spans_raw["0_"+p[1]]);
                    }


                    /*if (pure(spans["0_"+p[1]].innerText) === pure(story[i][3])) {

                    } else {
                        console.log("not equal "+i+" "+p[1]+" "+spans["0_"+p[1]].innerText);
                    }*/
                } else {
                    console.log("error "+i);
                }
                //ind++;
            } else {
                //console.log("error "+i);
                //check
                //ind = parseInt(p[1])-1;
                if (pure(story[i][3]) === pure(spans_raw["0_"+p[1]])) {

                } else {
                    console.log("not equal raw text with what was sended: "+i+" "+p[1]+" "+spans_raw["0_"+p[1]]);
                }

                real_text = get_rid_of_markup(spans_what_we_see[p[1]]);
                if (pure(real_text) === pure(story[i][3])) {

                } else {
                    console.log("not equal real text with what was sended: "+i+" "+p[1]+" "+real_text);
                }

                if (pure(real_text) === pure(spans_raw["0_"+p[1]])) {

                } else {
                    console.log("not equal real text with raw text:"+i+" "+p[1]+" "+real_text+" : "+spans_raw["0_"+p[1]]);
                }
                /*if (pure(spans["0_"+p[1]].innerText) === pure(story[i][3])) {

                } else {
                    console.log("not equal2 "+i+" "+p[1]+" "+spans["0_"+p[1]].innerText);
                }*/
                //ind += (p[1]-p2[1]);
            }


            prev_middle_sended_index = p[1];
        }

        prev = story[i];
    }
}

