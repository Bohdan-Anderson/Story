window.onload = start;


var temp = {"name":["bohdan","anders"],"location":["oakville","ontartio"]}



var counter = 0;
var words;

function focus(){
	document.getElementById("input").select();	
}

function start(){
	setTimeout(intro, 1);
	focus();
}

window.onclick = focus;
function enterTest(myElement,Content){
	var key = 0;
	if(window.event){
		key=window.event.keyCode;
	}
	else{
		key=event.which;
	}
	if(key == 13){
		words = Content[counter][3];		
		addText(words,counter);
		return true;
	} else {
		return false;
	}
}

function softWrite(outText){
	var div = document.getElementById("story");
	div.innerHTML +=  outText;	
	return true;		
}

function addText(){
	var text =  document.getElementById("input");
	var textsplit = text.value.split(" ");
	var goToScene = wordInObject(textsplit,words);
	if(goToScene>=0){
		softWrite("<br>" + text.value);			
		softWrite(Content[counter][4]);	

		if(goToScene == 0){
			if(Content.length > counter+1){	
				++counter;
				softWrite(Content[counter][2]);
			}		
		} else {
			counter = goToScene;
			softWrite(Content[counter][2]);
		}
	}
	text.setAttribute("value","");
}

//will go as deep as needed, this is a itterative function
function wordInObject(input,object){
	endvalue = -1;
	for(var a=0; a<input.length;++a){
		if(object[input[a]] != undefined){
			if(typeof object[input[a]] == "number"){
				endvalue = object[input[a]];
			} else if(typeof object[input[a]] == "object"){
				return wordInObject(input,object[input[a]]);
			}
		}
	}
	return(endvalue)
}

function intro(){
	softWrite(Content[counter][2]);
}

