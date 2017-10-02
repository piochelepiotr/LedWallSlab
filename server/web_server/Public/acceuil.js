$(function(){

    var numberOfSlabsForm = $("#slabsNumber");
    var slabsDiv = $("#slabs");
    var widthForm = $("#width");
    var heightForm = $("#height");
    var horizontalContainer = $('.horizontalContainer');
    var verticalContainer = $('.verticalContainer');

     $("form :input").change(function(){        //If any input is changed, we re-build the graphics
         var widthNewValue = widthForm.val();     // the new value entered in the width form
         var heightNewValue = heightForm.val();
         var totalOfSlabs = numberOfSlabsForm.val();  //the new total of slabs
         var slabsUnassigned = numberOfSlabsForm.val();     //var that will be useful during the buildinng process
         verticalContainer.empty();                     //we make sure that the former configuration is deleted
         for(var i = 0; i < heightNewValue; i++)         //i will be the index of the line in the matrix
             {
                 verticalContainer.append('<div name="horizontalContainer" class="horizontalContainer" id ="horizontalContainer'+(i+1)+'">');  //we create a horizontal div that will contain hte mini containers in which there will possibly be slabs
                 for(var j = 0; j < widthNewValue; j++)  //j is the index of the column in the matrix
                   {
                        horizontalContainerMini = $('#horizontalContainer'+(i+1));   //getting a Jquery object from the right horizontal div
                        var miniContainerAdded =$('<div name="miniContainer" class="miniContainer" id="conteneur'+(i+1)+'.'+(j+1)+'"></div>'); //we create the mini containers
                        horizontalContainerMini.append(miniContainerAdded);
                        if (slabsUnassigned>0)   //By default, we place the slabs from left to right and from the top to the bottom of the matrix, till there's no slab left
                          {
                            miniContainerAdded.append('<div id="slabImage'+Math.abs(slabsUnassigned-totalOfSlabs-1)+'" class="slabImage" > <p> '+Math.abs(slabsUnassigned-totalOfSlabs-1)+' </p> </div>');
                            slabsUnassigned = slabsUnassigned-1;  // one more slab has been placed, the total of slabs unassigned to a mini container decreases
                            //we can now update the position of the slab in the appropriate form
                            $("#slabx"+(Math.abs(slabsUnassigned-totalOfSlabs+1))).val(j*18);  //the value in the form is the pixel index. Each slab has 18 pixels in width and height, so we multiply by 18.
                            $("#slaby"+(Math.abs(slabsUnassigned-totalOfSlabs+1))).val(i*18);
                          }
                   }
                 verticalContainer.append('</div>'); //the vertical container is fully filled, we can now close it.
             }
             //We have created new containers. We must set them as droppable to be able to receive the draggable slabs
             $(".miniContainer").droppable({ drop:function(event, ui){
              //we set the value of the appropriate form according to the position of the slab : if a slab has been dropped in a mini container, its position is updated automatically
             $("#slabx"+(ui.draggable.attr("id").split('Image')[1]-1)).val((($(this).attr("id").split('.')[0].split('r')[1])-1)*18);
             $("#slaby"+(ui.draggable.attr("id").split('Image')[1]-1)).val((($(this).attr("id").split('.')[1])-1)*18);
              }});
              //We have created new slabs. We must set them as draggable to be able to modify the configuration by drag and drop
             $('.slabImage').draggable({snap:'.miniContainer'});
       });


       var slabsNumber = $('#slabsNumber');
       var slabs = $('#slabsForm');
       $('#slabsNumber').change(function(){  // if the number of slabs has been modified, by either the user or by loading a saved configuration, we must rebuild the graphic model
         slabsNumberChanged();
       });

       function slabsNumberChanged()   //the function handling a modification in the number of slabs form
          {
             var slabsx = document.getElementsByName('slabx');
             var slabsy = document.getElementsByName('slaby');
             var slabs = document.getElementById('slabsForm');
             var newValue = document.getElementById('slabsNumber').value;
             if(newValue > slabsx.length)
                 {
                     for(var i = slabsx.length; i < newValue; i++)
                       {
                            slabsForm.innerHTML += '<p><label>Dalle '+(i+1)+'</label> x : <input type="number" name="slabx" id="slabx'+i+'" min="0" required />  y : <input type="number" name="slaby" id="slaby'+i+'" min="0" required /> </p>';
                       }
                  }
             else
                 {
                     slabsForm.innerHTML = '';
                     for(var i = 0 ; i < newValue; i++)
                       {
                            var x = document.getElementById('slabx'+i);
                            var y = document.getElementById('slaby'+i);
                            slabsForm.innerHTML += '<p><label>Dalle '+(i+1)+'</label> x : <input type="number" name="slabx" id="slabx'+i+'" min="0" value="'+x+'" required />  y : <input type="number" name="slaby" id="slaby'+i+'" min="0" value="'+y+'" required /> </p>';
                       }
                 }
          };

          var buildSlabsButton = $('#buildSlabs');

          buildSlabsButton.click(function(){     //function handling the building of the graphic model according to the data entered in the slabs forms.
            var widthNewValue = widthForm.val();
            var heightNewValue = heightForm.val();
            var totalOfSlabs = numberOfSlabsForm.val();
            verticalContainer.empty();
            for(var i = 0; i < heightNewValue; i++)     //we build the horizontal containers and mini containers.
                 {
                     verticalContainer.append('<div name="horizontalContainer" class="horizontalContainer" id ="horizontalContainer'+(i+1)+'">');
                     for(var j = 0; j < widthNewValue; j++)
                       {
                           horizontalContainerMini = $('#horizontalContainer'+(i+1));
                           var miniContainerAdded =$('<div name="miniContainer" class="miniContainer" id="conteneur'+(i+1)+'.'+(j+1)+'"></div>');
                           horizontalContainerMini.append(miniContainerAdded);
                            for (var slabId = 0; slabId<totalOfSlabs; slabId++){
                              //we get back the position of each slab (x and y)
                              var x = $('#slabx'+slabId).val();
                              var y = $('#slaby'+slabId).val();
                              if (j*18<=x && x<(j+1)*18 && i*18<=y && y<(i+1)*18) //we check if the slab we are dealing with has a position that belongs to the current miniContainer.
                                                                                //If it's the case, we can create a slab in this mini container
                              {
                                miniContainerAdded.append('<div id="slabImage'+(slabId+1)+'" class="slabImage" > <p> '+(slabId+1)+' </p> </div>');
                              }
                            }
                       }
                     verticalContainer.append('</div>');
                 }
                 //We have created new containers. We must set them as droppable to be able to receive the draggable slabs
                 $(".miniContainer").droppable({ drop:function(event, ui){
                  //we set the value of the appropriate form according to the position of the slab
                 $("#slabx"+(ui.draggable.attr("id").split('Image')[1]-1)).val((($(this).attr("id").split('.')[0].split('r')[1])-1)*18);
                 $("#slaby"+(ui.draggable.attr("id").split('Image')[1]-1)).val((($(this).attr("id").split('.')[1])-1)*18);
                  }});
                  //We have created new slabs. We must set them as draggable to be able to modify the configuration by drag and drop
                 $('.slabImage').draggable({snap:'.miniContainer'});
          });

          var loadFromJSONButton = $('#loadFromJSON');
          //the function handling the load of a saved configuration
          loadFromJSONButton.click(function(){
            var xmlhttp;
            if (window.XMLHttpRequest) {
              xmlhttp = new XMLHttpRequest();
            } else {
              // code for older browsers
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
           }
            xmlhttp.onreadystatechange = function() {
              if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {  //mandatory conditions to make sure the request has been correctly sent
              doc = eval('('+xmlhttp.responseText+')');      //we get back the saved configuration which is written in Json, the eval function parse it
              //we first get back the meta data (number of slabs, width and height) and fill the appropriate form.
              numberOfSlabsForm.val(parseInt(doc.meta.total));
              widthForm.val(parseInt(doc.meta.width));
              heightForm.val(parseInt(doc.meta.height));
              slabsNumberChanged();       //the slab number has changed, we must create a new graphic model fitting the loaded data
              for (var i=0; i<doc.config.length; i++)
              {
                  var slabx = document.getElementById("slabx"+i);
                  var slaby = document.getElementById("slaby"+i);
                  slabx.value = parseInt(doc.config[i].x);  //we fill the position form of each slab with the corresponding data in the saved configuration
                  slaby.value = parseInt(doc.config[i].y);
              }
            }
          };
          xmlhttp.open("GET", "hello.txt", true);
          xmlhttp.send();
        });

          })
