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
function new_test() {
    var final_text, l, myhtml_result,spans_what_we_see, prev, prev_middle_sended_index, sended_chunk;
    var pure = function (phrase) {
        var str = phrase.trim();
        str = str.replace(/[^a-z0-9' ]/gi, '').toLowerCase();
        str = str.replace(/'[a-z]+ /gi," ");
        return str+" ";

    };
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
    };
    var compare = function (sended_chunk,from,i) {
        var html_result = myhtml_result.substring(from, from+sended_chunk.length);
        var final_result = final_text.substring(from, from+sended_chunk.length);

        if (sended_chunk !== html_result) {
            console.log("sended_chunk !== html_result :"+i+":"+sended_chunk+":"+html_result);
        }
        if (html_result !== final_result) {

            console.log("html_result !== final_result :"+i+":"+html_result+":"+final_result);
        }
        if (sended_chunk !== final_result) {
            console.log("sended_chunk !== final_result :"+i+":"+sended_chunk+":"+final_result);
        }
        return from+sended_chunk.length;
    };
    final_text = "";
    l = Object.keys(unblocked_html).length;
    for (var i = 0;i <l; i++) {
        var key = "0_"+i;
        var text = pure(unblocked_html[key]);
        final_text += text;
    }
    //final_text = final_text.replace(/'[a-z]+ /gi," ");
    myhtml_result = "";
    spans_what_we_see = document.querySelector(".transcription").children;
    for (var j = 0; j < spans_what_we_see.length; j++) {
        myhtml_result += pure(get_rid_of_markup(spans_what_we_see[j]));
    }
    //myhtml_result = myhtml_result.replace(/'[a-z]+ /gi," ");
    prev_middle_sended_index=1;
    var from = 0;
    var prev = [0,"0_0"];
    for (var i = 0; i < story.length; i++) {
        var p = story[i][1].split("_");
        var p2 = prev[1].split("_");
        /*if ((parseInt(p[1])+4)-story[i][0]!==1) {
            console.log((parseInt(p[1])+4)+"_"+story[i][0]);
        }*/
        if (p[1]-prev_middle_sended_index > 1) {
            console.log("increment "+i);
        }

        if (i===0) {
            sended_chunk = pure(story[i][2]);
            from = compare(sended_chunk,from , i);
        }
        sended_chunk = pure(story[i][3]);
        from = compare(sended_chunk,from , i);

        if (i>0) {
            if (p[1]-p2[1] === 1) {
                if (pure(story[i][2]) === pure(prev[3]) && pure(story[i][3]) === pure(prev[4])) {

                } else {
                    console.log("error "+i);

                }
                //ind++;
            } else {
                console.log(">1 jump");
            }
        }

        prev_middle_sended_index = p[1];
        prev = story[i];
    }

}
function stringalign(ainstr, binstr, keys_length, raw_punct_key2array, raw_punct_query_array,omit2key=false)
{
	var mispen=1, gappen=1, skwpen=0;
   var ain = ainstr;//.split(' ');
   var bin = binstr;//.split(' ');
   //var my_answer = [];
   //var my_final_answer = [];
	var number_of_matches = 0;
	var punctuation
   var i, j ,k;
   var dn,rt,dg;
   var ia = ain.length, ib = bin.length;
   var aout=[]; // .resize(ia+ib);
   var bout=[];
   var summary=[];
   var cost=[];
   var marked=[];
   for(n=0 ; n < ia+1 ;++n) {
       cost[n] = new Array(ib+1);
       marked[n] = new Array(ib+1);
   }

   cost[0][0] = 0.;
   for (i=1;i<=ia;i++) cost[i][0] = cost[i-1][0] + skwpen;
   for (i=1;i<=ib;i++) cost[0][i] = cost[0][i-1] + skwpen;
   for (i=1;i<=ia;i++) for (j=1;j<=ib;j++) {
       dn = cost[i-1][j] + ((j === ib)? skwpen : gappen);
       rt = cost[i][j-1] + ((i === ia)? skwpen : gappen);
       dg = cost[i-1][j-1] + ((ain[i-1] === bin[j-1])? -1. : mispen);
       cost[i][j] = Math.min(dn,rt,dg);
   }
   i=ia; j=ib; k=0;
   while (i > 0 || j > 0) {
       marked[i][j]=1;
       dn = rt = dg = 9.99e99;
       if (i>0) dn = cost[i-1][j] + ((j===ib)? skwpen : gappen);
       if (j>0) rt = cost[i][j-1] + ((i===ia)? skwpen : gappen);
       if (i>0 && j>0) dg = cost[i-1][j-1] + ((ain[i-1] === bin[j-1])? -1. : mispen);
       if (dg <= Math.min(dn,rt)) {
           aout[k] = ain[i-1];
           bout[k] = bin[j-1];


           summary[k++] = ((ain[i-1] === bin[j-1])? '=' : '!');
           if (summary[k-1]==="=") {
           		//my_answer.push([i-1, j-1]);
           		//my_final_answer.push(ain[i-1]);
				number_of_matches++;
		   }
           if (summary[k-1]==="!") {

		   }
           i--; j--;
       }
       else if (dn < rt) {
           aout[k] = ain[i-1];
           bout[k] = '-';
           summary[k++] = '-';
           //my_final_answer.push(ain[i-1]);
           i--;
       }
       else {
           aout[k] = '-';
           bout[k] = bin[j-1];
           summary[k++] = '-';
           //my_final_answer.push(bin[j-1]);
           j--;
       }
       marked[i][j]=1;
    }

	var new_key2_value = "";
	var first_match = false;
	var matches = 0;
	var after_last_match = false;
	//var key1_match = false;

    for (i=0;i<k/2;i++) {
        var t = aout[k-1-i];
        aout[k-1-i] = aout[i];
        aout[i]=t;

        t=bout[k-1-i];
        bout[k-1-i] = bout[i];
        bout[i]=t;

        t=summary[k-1-i];
        summary[k-1-i]=summary[i];
        summary[i]=t;

    }
    //i can do all logic here
		/*
		* [word1|word2|word3|word4][word5|word6|word7|word8|word9]-
		*             |word3|word4  word5|word6|word7|-    |word9|word10
		* -     |-    |=    |=     |=    |=    |=    |-    |=    |-
		*
		* [word1|word2|word3|word4][word5|word6|word7|-    |word9]-
		*             |word3|word4  word5|word6|word7|word8|word9|word10
		* -     |-    |=    |=     |=    |=    |=    |-    |=    |-
		*															CASE 2
		*[word1|word2|word3|word4][word5|word6|word7|word9]-
		*            |word3|word4  word5|word6|word7|word8|word10|word11
		* -    |-    |=    |=     |=    |=    |=    |!    |-     |-
		* 												     CASE 1

		*[word1|word2|word3|word4][word5|word6|word7|-    |word9]-
		*                               |word6|word7|word8|word9|word11
		* -    |-    |-    |-     |-    |=    |=    |-    |=    |-
		*
		*[word1|word2|word3|word4][word5|word6|word7|word8|word9]
		*            |word3|word4  word5|word6|word7|word8|-    |
		* -    |-    |=    |=     |=    |=    |=    |-    |=    |
		*
		*
		*

		* */


    aout.size=k; bout.size=k; summary.size=k;
	var index_of_query_rawword = 0;
	for (var i=0; i < summary.length; i++){

		if (i >= keys_length) {
			if (aout[i] !== "-" && bout[i] === "-" && first_match === false) {
				//new_key2_value += aout[i]+" ";//initial padding(before first match of query)/final padding(after final last match of query)
				new_key2_value += raw_punct_key2array[i-keys_length]+" ";
			}
			else if (aout[i] !== "-" && bout[i] === "-" && first_match === true) {
				new_key2_value += "";//deletion by query string
			}
			else if (summary[i] === "=") {
				first_match = true;
				//new_key2_value += aout[i]+" ";
				new_key2_value += raw_punct_key2array[i-keys_length]+" ";
				matches++;
				if (matches===number_of_matches) {//total number of matches for key1+key2
					first_match = false;
					after_last_match = true;
				}
				index_of_query_rawword++;
			}
			else if (summary[i] === "!" && after_last_match === false) {

                if (bout[i].length < aout[i].length) {
                    if (aout[i].substring(0,bout[i].length) === bout[i]) {
                        new_key2_value += raw_punct_query_array[index_of_query_rawword]+" ";
                    }
                } else if (bout[i].length > aout[i].length ){
                    if (bout[i].substring(0,aout[i].length) === aout[i]) {
                        new_key2_value += raw_punct_query_array[index_of_query_rawword]+" ";
                    }
                }
                index_of_query_rawword++;
            }
			else if (summary[i] === "!" && after_last_match === true) {//CASE 1
				//new_key2_value += aout[i]+" "+bout[i]+" ";
				new_key2_value += raw_punct_key2array[i-keys_length]+" "+raw_punct_query_array[index_of_query_rawword]+" ";
				index_of_query_rawword++;
			}
			else if (aout[i] === "-" && bout[i] !== "-" && (first_match === true || (after_last_match === true && omit2key===false) || (after_last_match === false && omit2key===true))) {//insertion by query or CASE 2
				//new_key2_value += bout[i]+" ";
				new_key2_value += raw_punct_query_array[index_of_query_rawword]+" ";
				index_of_query_rawword++;
			}

		} else if(summary[i] === "=") {
			first_match = true;
			matches++;
			if (matches===number_of_matches) {//total number of matches for key1+key2
				first_match = false;
				after_last_match = true;
			}
			index_of_query_rawword++;

		} else if (bout[i] !== "-") {
			index_of_query_rawword++;
		}
	}
   console.log(aout.join("|").replace(/ /gi, "-"));
   console.log(bout.join("|").replace(/ /gi, "-"));
   console.log(summary.join("|").replace(/ /gi, "-"));

   //console.log(my_answer);
	return new_key2_value.replace(/\s{2,}/g, ' ');
}

function test_nw() {
    var array_of_test_strings = [];

    array_of_test_strings.push(["word1 word2 word3 word4","word5 word6 word7 word8 word9","word3 word4 word5 word6 word7 word9 word10"]);
    array_of_test_strings.push(["word1 word2 word3 word4","word5 word6 word7 word9", "word3 word4 word5 word6 word7 word8 word9 word10"]);
    array_of_test_strings.push(["word1 word2 word3 word4","word5 word6 word7 word9","word3 word4 word5 word6 word7 word8 word10 word11"]);
    array_of_test_strings.push(["word1 word2 word3 word4","word5 word6 word7 word9","word6 word7 word8 word9 word11"]);
    array_of_test_strings.push(["word1 word2 word3 word4","word5 word6 word7 word8 word9","word3 word4 word5 word6 word7 word8"]);



    for(var i=0;i < array_of_test_strings.length; i++) {

        var key1 = array_of_test_strings[i][0].split(" ");
        var key2 = array_of_test_strings[i][1].split(" ");
        var query = array_of_test_strings[i][2].split(" ");
        var reference = key1.concat(key2);


        console.log(stringalign(reference, query, key1.length));
    }
}

test_nw();


var raw_punct_key2array = "".split(" ");
//if (already_sended[key2] === "") {
		    //raw_punct_key2array = already_sended[key2].split(" ");
		    raw_punct_key2array = [];
		    //var k1l = 4;
        //} else {
        // var l = already_sended_key1_array.length;
        // }
		var raw_punct_query_array = "word3 word4 word5".split(" ");

		var already_sended_key1 = phrase_punctuation_accounting("word1 word2 word3 word4");
		var already_sended_key2 = phrase_punctuation_accounting("");

		//already_sended[key1] = already_sended[key1].replace(/ ,/gi, ',');
		//already_sended[key2] = already_sended[key2].replace(/ ,/gi, ',');


		var already_sended_key1_array = already_sended_key1.split(" ");

		if (""==="") {
		    var already_sended_key2_array = [];
        } else {
		    var already_sended_key2_array = already_sended_key2.split(" ");
        }


		var already_sended_array = already_sended_key1_array.concat(already_sended_key2_array);

		var new_update = phrase_punctuation_accounting("word3 word4 word5");
		var new_update_array = new_update.split(" ");



stringalign(already_sended_array, new_update_array, already_sended_key1_array.length, raw_punct_key2array, raw_punct_query_array);

function strings_overlap(true_value, serach_string) {
	var start = 0,subphrase1,subphrase2;

	if (true_value === serach_string) {
		return false;
	}

	var space_pos = true_value.indexOf(" ",start);

	while (space_pos !==-1) {
		subphrase1 = true_value.substring(start);//shrincs
		subphrase2 = serach_string.substring(0,subphrase1.length);
		if (subphrase1 === subphrase2) {
			return subphrase2;
		}

		start+=1;
		space_pos = true_value.indexOf(" ",start);
	}
	return false;
}
function overlapping2() {
    console.log(111);
	var key3_value = phrase_punctuation_accounting("changing. ");
	var key2_value = phrase_punctuation_accounting("when it can, be avoided, genetics is changing. ");

	var overlap = strings_overlap(key2_value, key3_value);
	if (overlap!== false) {
		var first_part = "changing. ".substring(0,overlap.length);

		var punctuation_number = (first_part.match(/,|\.|\?|\!/gi)||[]).length;

		var res = "changing. ".substring(overlap.length+punctuation_number).trim();
		if (res===".") {
			res = "";
		} else {
			res += " ";
		}
		console.log(res);


	}
}


function strings_overlap(true_value, serach_string) {
    console.log(11);
	var start = 0,subphrase1,subphrase2;

	if (true_value === serach_string) {
		return false;
	}

	var space_pos = true_value.indexOf(" ",0);
	subphrase1 = true_value.substring(0);//shrincs
    var i = 0;
	while (space_pos !==-1) {
		//subphrase1 = true_value.substring(start);//shrincs
		subphrase2 = serach_string.substring(0,subphrase1.length);
		if (subphrase1 === subphrase2) {
			return subphrase2;
		}

		//start+=1;
		//

		subphrase1 = true_value.substring(space_pos+1);
		space_pos = true_value.indexOf(" ",space_pos+1);
        if (i>50) {
            break;
        }
        i++;
	}
	return false;
}

strings_overlap("word1 word2 word3", "word2 word3 word4")