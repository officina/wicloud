/* (C) 2017 Wi4B S.r.l. P.IVA : 02951211206 Mailto: info@wi4b.it
 #This document contains confidential and proprietary information.
 #Reproduction and / or disclosure through any means is prohibited unless expressed, written consent of authorized representative of Wi4b s.r.l. is obtained
 */


lightProfileViewer=function(){
    var that = this;
    this.homePage = null;
    var dhxLayout = null;
    this.mod_slots = "../modules/mod_slots.php";
    this.lightProfileId = 0;
    this.lightProfiles = {};
    this.lightBoxVisible = false;
    this.LightProfileController = null;
    this.lightProfileId = null;
    this.init = function () {
        this.dhxLayout = new dhtmlXLayoutObject({parent:"lpViewer",pattern: "1C"});
        this.dhxWins = this.dhxLayout.dhxWins;
        this.dhxWins.setImagePath("/assets/app/js/libs/dhtmlxsuite/imgs/");
        this._initContent();
    };

    this._initContent = function () {

        this.light_profile_slots = new dhtmlXDataStore();
        this.light_profile_slots.data.scheme({
            id:"",
            slot:"",
            name:"",
            description:"",
            don:"",
            ton:"",
            tof:"",
            pw0:"",
            pw1:"",
            pw2:"",
            eas:"",
            ecr:"",
            emo:"",
            timestamp:"",
            enabled:""
        });


        this.dhxLayout.cells("a").setText("Slots");
        //this.dhxLayout.cells("c").setText("Overview");


        this.dhxLayout.cont.obj._offsetWidth = -40; // right margin
        this.dhxLayout.cont.obj._offsetHeight = -40; // bottom margin

        this.dhxLayout.setAutoSize("a", "a");
        this.dhxLayout.setSizes();

        this.dhxLayout.cells("a").attachHTMLString('<div id="gantt_here" style="width:100%; height:100%;"></div>');
        this._initGantt();

        gantt.init("gantt_here");

        //gantt._min_date = new Date(2000, 11, 31, 00, 00);
        //gantt._max_date = new Date(2001, 0, 2, 24, 00);


        gantt.attachEvent("onLoadEnd", function(){
            //var first = gantt.getTaskByTime()[0];
            //gantt.showLightbox(first.id);
        });

        //gantt.load("common/slots.json", "json");

        this.toolbarSlots = this.dhxLayout.cells("a").attachToolbar();
        this.toolbarSlots.setIconsPath("/assets/app/media/img/toolbar/");
        var toolbarXML = '<toolbar id="1">\
            <item id="channel_add" type="button" img="bar_channel_add.gif" imgdis="bar_channel_add_dis.gif"   title="Add Slot" />\
            <item id="channel_edit" type="button" img="bar_channel_edit.gif" imgdis="bar_channel_edit_dis.gif"  title="Edit Slot" />\
            <item id="channel_remove" type="button" img="bar_channel_remove.gif" imgdis="bar_channel_remove_dis.gif" enabled="false" title="Remove Slot Completely" />\
            <item id="sep01" type="separator" />\
            <item id="channel_move_up" type="button" img="bar_channel_move_up.gif" imgdis="bar_channel_move_up_dis.gif" enabled="false" title="Move Slot Up" />\
            <item id="channel_move_down" type="button" img="bar_channel_move_down.gif" imgdis="bar_channel_move_down_dis.gif" enabled="false" title="Move Slot Down" />\
            <item id="sep03" type="separator" />\
            <item id="channel_save" type="button" img="bar_channel_save.gif" imgdis="bar_channel_save_dis.gif" enabled="true" title="Save Slot" />\
            <item id="channel_reset" type="button" img="bar_channel_reset.gif" imgdis="bar_channel_reset_dis.gif" enabled="true" title="Reset all slots" />\
            </toolbar>';

        this.toolbarSlots.loadXMLString(toolbarXML);

        this.toolbarSlots.attachEvent("onClick", function (id) {
            that._doOnToolbarSlotsClick(id);
        });
        that.reloadLightProfileSlots();

    };

    this.reloadLightProfileSlots = function() {
        that.LightProfileController.reloadLightProfileSlots(that.lightProfileId,that,
            function(data,reference) {
                reference.extractLightProfileSlots(data);
                reference.reloadGantt();
            }
        );
    };

    this.extractLightProfileSlots = function(inputData) {
        that.lightProfiles[that.lightProfileId] = {}
        that.lightProfiles[that.lightProfileId].slots = [];
        for (var key in inputData) {
            var lprofileSlot = inputData[key];
            var lightProfileSlot = new LightProfileSlot(lprofileSlot);
            that.lightProfiles[that.lightProfileId].slots.push(lightProfileSlot);
        }
    };

    this._initGantt = function() {

        gantt.form_blocks["lightLevel"] = {
            render: function (sns) {
                return '<div class="gantt_slider"><div><input type="text" readonly="true"/></div></div>';
            },
            set_value: function (node, value, task, data) {
                if (!node._slider) {
                    node._slider = new dhtmlxSlider({
                        parent: node,
                        size: 200,
                        skin: "ball",
                        max: 100,
                        step: data.step ? data.step : 1
                    });
                    node._slider.setImagePath("/assets/app/js/libs/dhtmlxsuite/imgs/");
                    node._slider.setSkin("dhx_skyblue");
                    node._slider.init();

                    node._count = document.createElement('div');
                    node._count.className = "gantt_slider_value";
                    node._slider.con.appendChild(node._count);
                    node._slider.con.style.overflow = "visible";

                    var slider_id = node._slider.attachEvent("onChange", function (newValue, sliderObj) {
                        node._count.innerHTML = newValue + "%";
                    });
                    var id = gantt.attachEvent("onAfterLightbox", function () {
                        try {
                            node._slider.detachEvent(slider_id);
                            node.removeChild(node._slider.con);
                            node._slider.con
                            node._slider = null;
                            this.detachEvent(id);
                        }
                        catch(Exception) {
                            console.log(Exception);
                        }
                    });

                }

                if (isNaN(task.progress)) task.progress = 1;
                if (task.progress || task.progress == 0) {
                    node._slider.setValue(parseInt(task.progress * 100));
                    node._count.innerHTML = parseInt(task.progress * 100) + "%";
                }
            },
            get_value: function (node, task) {
                return node._slider ? node._slider.getValue() / 100 : 0;
            },
            focus: function (node) {
            }
        };

        gantt.form_blocks["motionParameters"] = {
            render: function (sns) {
                return '<div id="motionParameters">' +
                    '<span class="motion_input">Duration<input type="text" name="motionDuration" id="motionDuration"> </span><span class="motion_input">Delay<input type="text" name="motionDelay" id="motionDelay"></span>' +
                    '<div class="gantt_slider">'
                '<div class="motion_slider_div"><div><input type="text" readonly="true"/></div></div>' +
                '</div>';
            },
            set_value: function (node, value, task, data) {
                if (!node._slider) {
                    var sliderDiv = node.childNodes[2];
                    node._slider = new dhtmlxSlider({
                        parent: sliderDiv,
                        size: 200,
                        skin: "ball",
                        max: 100,
                        step: data.step ? data.step : 1
                    });

                    node._slider.setImagePath("/assets/app/js/libs/dhtmlxsuite/imgs/");
                    node._slider.setSkin("dhx_skyblue");
                    node._slider.init();

                    node._count = document.createElement('div');
                    node._count.className = "gantt_slider_value";
                    node._slider.con.appendChild(node._count);
                    node._slider.con.style.overflow = "visible";

                    var slider_id = node._slider.attachEvent("onChange", function (newValue, sliderObj) {
                        node._count.innerHTML = newValue + "%";
                    });
                    var id = gantt.attachEvent("onAfterLightbox", function () {
                        try {
                            node._slider.detachEvent(slider_id);
                            sliderDiv.removeChild(node._slider.con);
                            node._slider.con
                            node._slider = null;
                            this.detachEvent(id);
                        }
                        catch(Exception) {
                            console.log(Exception);
                        }
                    });

                    if ($!=null) console.log($);
                    else console.log("Cannot find $");
                    $('#slotMotionCheck').change(function() {
                        if($(this).is(":checked")) {
                            node.style.visibility = "";
                            $("#motionDuration").val(task.motionDuration);
                            $("#motionDelay").val(task.motionDelay);
                            node._slider.setValue(parseInt(task.motionLightLevel));
                            node._count.innerHTML = parseInt(task.motionLightLevel) + "%";
                        }
                        else {
                            node.style.visibility = "hidden";
                        }
                    });

                }
                if (isNaN(task.motionLightLevel)) task.motionLightLevel = 100;
                if (task.MotionEnabled) {
                    node.style.visibility = "";
                    $("#motionDuration").val(task.motionDuration);
                    $("#motionDelay").val(task.motionDelay);
                    node._slider.setValue(parseInt(task.motionLightLevel));
                    node._count.innerHTML = parseInt(task.motionLightLevel) + "%";
                }
                else {
                    node.style.visibility = "hidden";
                }
            },
            get_value: function (node, task) {
                return node._slider ? node._slider.getValue()  : 0;
            },
            focus: function (node) {
            }
        };

        /*gantt.config.columns = [
         {name:"Day", label:"Start time", width: 65 ,align: "center",template:function(obj){
         return that.getWorkingDayLabel(obj.start_date,obj.end_date,obj,true);} },
         {name:"start_date", label:"Start time", width: 65 ,align: "center",template:function(obj){
         return obj.start_date.format("HH:MM")} },
         {name:"end_date", label:"End time", width: 65, align: "center",template:function(obj){
         return obj.end_date.format("HH:MM")} },
         {name:"duration",   label:"Duration", width: 30,   align: "center" },
         {name:"add",        label:"", width: 40}
         ];*/

        function getHeaderDiv(task) {
            var topLine = '<div class="topLine">'+task.name+'</div>';
            var bottomLine = '<div class="bottomLine">'+that.getWorkingDayLabel(task.start_date,task.end_date,task,true)+'</div>';
            return '<div class="taskGridHeaderDiv">'+topLine+bottomLine+'</div>';
        };

        gantt.config.columns = [
            {name:"Name", label:"Slot", width: 65 ,align: "center",template:function(obj){
                return  getHeaderDiv(obj); } },
        ];



        gantt.config.lightbox.sections = [
            {name: "description", height: 80, map_to: "text", type: "textarea", focus: true},
            {name: "lightLevel", type: "lightLevel", map_to: "progress", step: 5},
            {name: "dayOn", height: 22, map_to: "dayOn", type: "select", onchange: that.manageDayOnDayOff, options: [
                {key:10, label: "All days"},
                {key:11, label: "Work days"},
                {key:12, label: "Weekend days"},
                {key:0, label: "Monday"},
                {key:1, label: "Tuesday"},
                {key:2, label: "Wednesday"},
                {key:3, label: "Thursday"},
                {key:4, label: "Friday"},
                {key:5, label: "Saturday"},
                {key:6, label: "Sunday"}
            ]},
            {name: "dayOff", height: 22, map_to: "dayOff", type: "select", options: [
                {key:0, label: "Monday"},
                {key:1, label: "Tuesday"},
                {key:2, label: "Wednesday"},
                {key:3, label: "Thursday"},
                {key:4, label: "Friday"},
                {key:5, label: "Saturday"},
                {key:6, label: "Sunday"}
            ]},
            {name: "time", height: 72, type: "time", map_to: "auto", time_format:["%d","%m","%Y","%H:%i"]},
            {name:"extraFeatures", height:16, type:"template", map_to:"extraFeatures_template"},
            {name:"motionParameters", height:16, type:"motionParameters", map_to:"motionLightLevel"}
        ];

        gantt.locale.labels.section_lightLevel = "Light level";
        gantt.locale.labels.section_dayOn = "Week day start";
        gantt.locale.labels.section_dayOff = "Week day end";
        gantt.locale.labels.section_duration = "Duration";
        gantt.locale.labels.section_extraFeatures = "Extra features";
        gantt.locale.labels.section_motionParameters = "Motion parameters";
        gantt.locale.labels.confirm_deleting = "Slot will be deleted permanently, are you sure?";

        function updateTaskFields(task) {
            if(that.lightBoxVisible) {
                if (!(task instanceof LightProfileSlot))  {
                    var lightProfileSlot = new LightProfileSlot(task);
                    lightProfileSlot.light_profile = parseInt(that.lightProfileId);
                    gantt.addTask(lightProfileSlot);
                    task = gantt.getTask(task.id);
                }
                var checkBox = $('#slotAstroCheck');
                console.log("----Updating Task-----");
                task.AstroEnabled = $('#slotAstroCheck').is(":checked");
                task.TwilightEnabled = $('#slotTwilightCheck').is(":checked");
                task.MotionEnabled = $('#slotMotionCheck').is(":checked");

                task.motionDelay = $("#motionDelay").val();
                task.motionDuration = $("#motionDuration").val();

                var values = gantt.getLightboxValues();
                task.calculateEndDate();
                console.log(values);
                console.log(task.start_date);
                console.log(task.end_date);
                console.log("----Updated Task------");

            }
            that._setPendingChanges(true);
        }


        /*gantt.addTaskLayer(function draw_planned(task) {

         var start = new Date();
         start.setTime(task.start_date.getTime());
         var end = new Date();
         end.setTime(task.end_date.getTime());

         var sizes = gantt.getTaskPosition(task, start, end);
         //var sizes = gantt.getTaskPosition(task, task.planned_start, task.planned_end);
         var el = document.createElement('div');
         el.className = 'baseline';
         el.style.left = sizes.left + 'px';
         el.style.width = sizes.width + 'px';
         el.style.background = "red";
         el.style.top = sizes.top + gantt.config.task_height  + 13 + 'px';

         return el;
         });*/



        gantt.addTaskLayer(function draw_planned(task) {
            if ((task instanceof LightProfileSlot)) task.calculateEndDate();
            if (task.start_date.getDate()!=task.end_date.getDate()) {
                console.log("Start date: "+task.start_date.getDate()+ " - End date: " +task.end_date.getDate());
                if(task.start_date.getHours()>task.end_date.getHours()){
                    var start = new Date(task.start_date.getFullYear(),task.start_date.getMonth(), task.start_date.getDate(), 0,0,0,0);
                    var end = new Date(task.start_date.getFullYear(),task.start_date.getMonth(), task.start_date.getDate(), task.end_date.getHours(),task.end_date.getMinutes(),0,0);

                    var sizes = gantt.getTaskPosition(task, start, end);
                    var el = document.createElement('div');
                    el.topmost=true;
                    el.className = 'baseline';
                    el.style.left = sizes.left + 'px';
                    el.style.width = sizes.width + 'px';
                    el.style.top = sizes.top +  12 + 'px';
                    return el;
                }
                else {
                    var start = new Date(task.start_date.getFullYear(),task.start_date.getMonth(), task.start_date.getDate(), 0,0,0,0);
                    var end = new Date(task.start_date.getFullYear(),task.start_date.getMonth(), task.start_date.getDate(), task.end_date.getHours(),task.end_date.getMinutes(),0,0);

                    var sizes = gantt.getTaskPosition(task, start, end);
                    var el = document.createElement('div');
                    el.topmost=true;
                    el.className = 'baseline';
                    el.style.left = sizes.left + 'px';
                    el.style.width = sizes.width + 'px';
                    el.style.top = sizes.top +  12 + 'px';
                    return el;
                }
            }
            else {
                console.log("Removing extralayer");
                var el = document.createElement('div');
                el.topmost=true;
                return el;
            }
            return false;
        });


        gantt.attachEvent("onAfterTaskAdd", function(id,task){
            console.log("Task added");
            updateTaskFields(task);
            return true;
        });

        gantt.attachEvent("onAfterTaskUpdate", function(id, task){
            console.log("Task update");
            updateTaskFields(task);
            return true;
        });

        gantt.attachEvent("onTaskSelected", function(id,item){
            if(isNaN(id)) {
                that.toolbarSlots.enableItem("channel_add");
                that.toolbarSlots.disableItem("channel_edit");
                that.toolbarSlots.disableItem("channel_remove");
                that.toolbarSlots.disableItem("channel_move_up");
                that.toolbarSlots.disableItem("channel_move_down");

            }
            else {
                that.toolbarSlots.enableItem("channel_add");
                that.toolbarSlots.enableItem("channel_edit");
                that.toolbarSlots.enableItem("channel_remove");
                that.toolbarSlots.enableItem("channel_move_up");
                that.toolbarSlots.enableItem("channel_move_down");
            }
        });

        gantt.attachEvent("onBeforeLightbox", function(id){
            console.log("Before Lightbox");
            var timeControl = gantt.getLightboxSection("time");
            for (var key = 0;key< timeControl.control.length;key++) {
                if (parseInt(key)==3 || parseInt(key)==7) continue;
                var childNode = timeControl.control[key];
                childNode.style.display = "none";
            }
            timeControl.node.style.textAlign = "left";


            var task = gantt.getTask(id);
            task.end_date.addDays(1);

            task.extraFeatures_template = '<input class="lightBoxCheckBoxes" id="slotAstroCheck" type="checkbox" name="astro"> Enable Astro clock \
				<input class="lightBoxCheckBoxes" type="checkbox" id="slotTwilightCheck" name="twilight"> Enable Twilight sensor \
				<input class="lightBoxCheckBoxes" type="checkbox" id="slotMotionCheck" name="motion"> Enable Motion';


            task.motionParameters_template = '<div id="motionParameters"><span class="motion_input">Duration<input type="text" name="duration"> </span><span class="motion_input">Delay<input type="text" name="duration"></span>    </div>  ';

            return true;
        });

        gantt.attachEvent("onLightbox", function(id){
            console.log("Lightbox");
            that.lightBoxVisible = true;
            that.manageDayOnDayOff();
            var task = gantt.getTask(id);
            //task.splitStart = 30;
            //task.splitEnd = 60;
            $('#slotAstroCheck').prop('checked', task.AstroEnabled);
            $('#slotTwilightCheck').prop('checked', task.TwilightEnabled);
            $('#slotMotionCheck').prop('checked', task.MotionEnabled);
            return true;
        });

        gantt.attachEvent("onAfterLightbox", function(id){
            console.log("After lightbox");
            that.lightBoxVisible = false;
            return true;
        });


        gantt.attachEvent("onAfterTaskMove", function(id, parent, tindex){
            that._setPendingChanges(true);
        });




        gantt.templates.time_picker = function(date){
            return gantt.date.date_to_str(gantt.config.time_picker)(date);
        };

        gantt.templates.date_grid = function(date){
            return gantt.date.date_to_str(gantt.config.task_date)(date);
        };

        gantt.templates.task_text=function(start, end, task){

            var bottomDiv = '<div class="taskBottomDiv">'

            if (task.MotionEnabled) {
                bottomDiv += "<div class='motionSensorBottom'></div>";
            }
            if (task.TwilightEnabled) {
                bottomDiv += "<div class='twilightSensorBottom'></div>";
            }
            if (task.AstroEnabled) {
                bottomDiv += "<div class='astroSensorBottom'></div>";
            }
            bottomDiv += '<div class="taskBottomDescription">' + that.getWorkingDayLabel(start,end,task) + '</div>';

            bottomDiv+="</div>";

            //var taskText = "" + (parseInt(task.$index) + 1) + " - " + task.text + " " + task.duration + " min" + bottomDiv;
            var taskText = task.duration + " min";
            return taskText + bottomDiv;
        };


        gantt.templates.lightbox_header = function(start,end,task){
            var label = "Slot "+ (parseInt(task.$index)+1)+" - ";
            return label + that.getWorkingDayLabel(start,end,task);

        };

        gantt.templates.task_date = function(date){
            return date.format("HH:MM");
            return gantt.date.date_to_str(gantt.config.task_date)(date);
        };

        gantt.templates.date_scale = function(date){
            return gantt.date.date_to_str(gantt.config.date_scale)(date);
        };


        gantt.templates.scale_cell_class = function(date){
            if(date.getHours()>16){
                return "night";
            }
        };

        gantt.config.task_height = 20;

        gantt.templates.task_class=function(start, end, task){
            if (task.splitStart)
                return "complex_gantt_bar";

            if (task.id == "61")
            {
                return "taskHalfSize"
            }
            return "";};


        /*gantt.templates.task_class=function(start, end, task){
         return "taskHalfSize";
         };*/



        gantt.config.dragOverLimits = true;
        gantt.config.show_links = false;
        //gantt.config.disableDragBeforeStart = false;
        gantt.config.scale_unit = "hour";
        gantt.config.step = 1;
        gantt.config.date_scale = "%H:%i";
        gantt.config.time_step = 1; //set scale to snap to
        gantt.config.round_dnd_dates = false; //disables snap to grid


        gantt.config.duration_unit = "minute";

        gantt.config.min_column_width = 50;
        gantt.config.min_duration = 1;
        //gantt.config.autosize = "xy";
        gantt.config.start_date = new Date(2001, 0, 1, 00, 00);
        gantt.config.end_date = new Date(2001, 0, 1, 24, 00);

        gantt.config.min_grid_column_width = 50;
        gantt.config.order_branch = true; //allows ordering of tasks
        gantt.config.order_branch_free = true; //allows ordering of tasks


        gantt.templates.leftside_text = function(start, end, task){
            return "";
            //return "<div class='motionSensor'></div>";
            var el = "<div class='sensorsContainer'>";

            if (task.MotionEnabled) {
                el += "<div class='motionSensor'></div>";
            }
            if (task.TwilightEnabled) {
                el += "<div class='twilightSensor'></div>";
            }
            if (task.AstroEnabled) {
                el += "<div class='astroSensor'></div>";
            }
            el+="</div>";
            return el;
        };

        gantt.attachEvent("onTaskDrag", function(id, mode, task, original){
            var modes = gantt.config.drag_mode;
            if(mode == modes.move || mode == modes.resize){
                //Round to net hour
                var minutesMore = task.start_date.getMinutes() % 60;
                if (minutesMore<=5)
                    task.start_date = new Date(task.start_date.getFullYear(),task.start_date.getMonth(), task.start_date.getDate(), task.start_date.getHours(),0,0,0);

                /*var minutes = (((task.start_date.getMinutes() + 7.5)/15 | 0) * 15) % 60;
                 var hours = ((((task.start_date.getMinutes()/105) + .5) | 0) + task.start_date.getHours()) % 24;

                 task.start_date = new Date(task.start_date.getFullYear(),task.start_date.getMonth(), task.start_date.getDate(), hours,minutes,0,0);
                 */
            }
            return true;
        });





        gantt.config.grid_resize = true;


    };

    this.manageDayOnDayOff = function(event) {
        var canModifyDayOff = true;
        if (!event)  canModifyDayOff = false;
        var dayOn = gantt.getLightboxSection("dayOn");
        var dayOff = gantt.getLightboxSection("dayOff");
        var display = "";
        if (canModifyDayOff) dayOff.setValue(dayOn.getValue());
        if (dayOn.getValue() >6) {
            display = "none";
        }
        dayOff.node.style.display=display; // editor area
        dayOff.node.previousSibling.style.display=display; //section header
        gantt.resizeLightbox(); //correct size of lightbox

    };

    this.getWorkingDayLabel = function(start,end,task,hideHours) {
        var label = "";
        if (!hideHours) hideHours = false;
        else hideHours = true;
        switch (parseInt(task.dayOn)) {
            case 0: label += "Mon "+ (hideHours?"":task.start_date.format("HH:MM")); break;
            case 1: label += "Tue "+(hideHours?"":task.start_date.format("HH:MM")); break;
            case 2: label += "Wed "+(hideHours?"":task.start_date.format("HH:MM")); break;
            case 3: label += "Thy "+(hideHours?"":task.start_date.format("HH:MM")); break;
            case 4: label += "Fri "+(hideHours?"":task.start_date.format("HH:MM")); break;
            case 5: label += "Sat "+(hideHours?"":task.start_date.format("HH:MM")); break;
            case 6: label += "Sun "+(hideHours?"":task.start_date.format("HH:MM")); break;
            case 10: label += "All days " + (hideHours?"":task.start_date.format("HH:MM")+ " - " + task.end_date.format("HH:MM")); break;
            case 11: label += "Work days " + (hideHours?"":task.start_date.format("HH:MM")+ " - " + task.end_date.format("HH:MM")); break;
            case 12: label += "Weekend days " + (hideHours?"":task.start_date.format("HH:MM")+ " - " + task.end_date.format("HH:MM")); break;
        }
        if (parseInt(task.dayOn)<=6 && parseInt(task.dayOff)<=6 && parseInt(task.dayOn) != parseInt(task.dayOff)) {
            switch (parseInt(task.dayOff)) {
                case 0: label += " - Mon "+(hideHours?"":task.end_date.format("HH:MM")); break;
                case 1: label += " - Tue "+(hideHours?"":task.end_date.format("HH:MM")); break;
                case 2: label += " - Wed "+(hideHours?"":task.end_date.format("HH:MM")); break;
                case 3: label += " - Thu  "+(hideHours?"":task.end_date.format("HH:MM")); break;
                case 4: label += " - Fri "+(hideHours?"":task.end_date.format("HH:MM")); break;
                case 5: label += " - Sat "+(hideHours?"":task.end_date.format("HH:MM")); break;
                case 6: label += " - Sun "+(hideHours?"":task.end_date.format("HH:MM")); break;
            }
        }
        return label;
    };

    this.getLightProfileSlotsFromGantt = function() {
        var tasksIds = gantt.getChildren(gantt.config.root_id);
        var tasks = [];
        for (var key in tasksIds) {
            var task = gantt.getTask(tasksIds[key]);
            try {
                task.slot = task.$index+1;
            }
            catch(Exception) {
                console.log(Exception);
            }
            tasks.push(task);
        }
        return tasks;
    };

    this.convertTasksToSlots = function() {
        var tasks = that.getLightProfileSlotsFromGantt();
        for (var key in tasks) {
            var task = tasks[key];
            var lightProfileSlot = new LightProfileSlot(task);
            lightProfileSlot.light_profile = parseInt(that.lightProfileId);
            lightProfileSlot.pw0 = isNaN(parseInt(lightProfileSlot.progress))?0:lightProfileSlot.progress*100;
            lightProfileSlot.pw1 = isNaN(parseInt(lightProfileSlot.progress))?0:lightProfileSlot.progress*100;
            lightProfileSlot.pw2 = isNaN(parseInt(lightProfileSlot.progress))?0:lightProfileSlot.progress*100;
            lightProfileSlot.pw3 = isNaN(parseInt(lightProfileSlot.progress))?0:lightProfileSlot.progress*100;
            lightProfileSlot.mi0 = isNaN(parseInt(lightProfileSlot.motionLightLevel))?0:lightProfileSlot.motionLightLevel;
            lightProfileSlot.mi1 = isNaN(parseInt(lightProfileSlot.motionLightLevel))?0:0;
            lightProfileSlot.mi2 = isNaN(parseInt(lightProfileSlot.motionLightLevel))?0:0;
            lightProfileSlot.mi3 = isNaN(parseInt(lightProfileSlot.motionLightLevel))?0:0;
            lightProfileSlot.fadeIn = isNaN(parseInt(lightProfileSlot.fadeIn))?0:lightProfileSlot.fadeIn;
            lightProfileSlot.fadeOut = lightProfileSlot.fadeIn;
            lightProfileSlot.motionFadeIn = parseInt(lightProfileSlot.fadeIn / 10);
            lightProfileSlot.motionFadeOut = parseInt(lightProfileSlot.fadeIn / 10);
            lightProfileSlot.motionFadeIn = lightProfileSlot.motionFadeIn>254?254:lightProfileSlot.motionFadeIn;
            lightProfileSlot.motionFadeOut = lightProfileSlot.motionFadeOut>254?254:lightProfileSlot.motionFadeOut;
            lightProfileSlot.motionDuration = isNaN(parseInt(lightProfileSlot.motionDuration))?10:parseInt(lightProfileSlot.motionDuration);
            lightProfileSlot.motionDelay = isNaN(parseInt(lightProfileSlot.motionDelay))?0:parseInt(lightProfileSlot.motionDelay);

            gantt.addTask(lightProfileSlot);
        }
    };

    this.convertSlotsToLightProfileSlots = function(slots) {
        for (var index in slots) {
            slots[index] = slots[index].getDict();
        }
        return slots;
    };

    this.reloadGantt = function() {
        try {
            if (that.lightProfileId!=0) {
                gantt.clearAll();
                for (var key in that.lightProfiles[parseInt(that.lightProfileId)].slots) {
                    var lightProfileSlot = that.lightProfiles[that.lightProfileId].slots[key];
                    gantt.addTask(lightProfileSlot);
                }
            }
            else {
                gantt.clearAll();
            }
            that._setPendingChanges(false);
        }
        catch(Exception ) {
            console.log(Exception);
        }

    };

    this._bindTM = null;
    this._bindTMTime = 10 * 60 * 1000;

    this._doOnSelectTreeNode = function (id) {
        var slotsUpdated = that.dhxTree.getUserData(id, "slotsUpdated");
        var inUse = false;
        var inUse = that.dhxTree.getUserData(id, "inUse");

        if (that.currentSelectedTreeModified) {
            alert("Save or revert configuration before selecting a new light profile");
            that.dhxTree.selectItem(that.lightProfileId,false,false);
        }
        else {
            that.lightProfileId = id;
            that.loadLightProfileSlots(id, slotsUpdated);

            if(isNaN(id)) {
                that.toolbarSlots.disableItem("channel_add");
                that.toolbarSlots.disableItem("channel_edit");
                that.toolbarSlots.disableItem("channel_remove");
                that.toolbarSlots.disableItem("channel_move_up");
                that.toolbarSlots.disableItem("channel_move_down");
                that.toolbarSlots.disableItem("channel_save");
                that.toolbarSlots.disableItem("channel_reset");

                that.dhxWebBar.disableItem("channel_remove");
                that.dhxWebBar.disableItem("channel_edit");
            }
            else {
                that.toolbarSlots.enableItem("channel_add");
                that.toolbarSlots.disableItem("channel_edit");
                that.toolbarSlots.disableItem("channel_remove");
                that.toolbarSlots.disableItem("channel_move_up");
                that.toolbarSlots.disableItem("channel_move_down");
                that.toolbarSlots.disableItem("channel_save");
                that.toolbarSlots.disableItem("channel_reset");
                if(inUse) that.dhxWebBar.disableItem("channel_remove");
                else that.dhxWebBar.enableItem("channel_remove");
                that.dhxWebBar.enableItem("channel_edit");
            }
        }
    };

    this._doOnToolbarSlotsClick = function (id) {
        switch (id) {
            case "channel_add":
                this._doSlotAdd();
                break;
            case "channel_edit":
                this._doSlotEdit();
                break;
            case "channel_remove":
                this._doSlotRemove();
                break;
            case "channel_move_up":
                this._doSlotMoveUp();
                break;
            case "channel_move_down":
                this._doSlotMoveDown();
                break;
            case "channel_save":
                this._doAllSlotSave();
                break;
            case "channel_reset":
                this.loadLightProfileSlots(that.lightProfileId);
                break;
        }
    };


    this._doOnToolbarClick = function (id) {
        switch (id) {
            case "channel_add":
                this._doNewLightProfileWindow();
                break;
            case "channel_edit":
                this._doEditLightProfileWindow();
                break;
            case "channel_remove":
                this._doRemoveLightProfileWindow();
                break;
        }
    };

    this._doSlotAdd = function() {
        gantt.createTask();
        that._setPendingChanges(true);
    };

    this._doSlotMoveUp = function() {
        var selectedId = gantt.getSelectedId();
        if (selectedId) {
            var taskIndex = gantt.getTaskIndex(selectedId);
            gantt.moveTask(selectedId, taskIndex-1>=0?taskIndex-1:0);
            that._setPendingChanges(true);
            gantt.refreshData();
        }
    };

    this._doSlotMoveDown = function() {
        var selectedId = gantt.getSelectedId();
        if (selectedId) {
            var taskIndex = gantt.getTaskIndex(selectedId);
            gantt.moveTask(selectedId, taskIndex+1);
            that._setPendingChanges(true);
            gantt.refreshData();
        }
    };

    this._doSlotRemove = function() {
        var selectedId = gantt.getSelectedId();
        if (selectedId) {
            gantt._dhtmlx_confirm(gantt.locale.labels.confirm_deleting, gantt.locale.labels.confirm_deleting_title, function () {
                gantt.deleteTask(selectedId);
                that._setPendingChanges(true);
                gantt.refreshData();
            })

        }
    };

    this._setPendingChanges = function (pendingChanges) {
        if(pendingChanges) {
            that.currentSelectedTreeModified = true;
            that.toolbarSlots.enableItem("channel_save");
            that.toolbarSlots.enableItem("channel_reset");
        }
        else {
            that.currentSelectedTreeModified=false;
            that.toolbarSlots.disableItem("channel_save");
            that.toolbarSlots.disableItem("channel_reset");
        }
    };

    this._doSlotEdit = function(rId) {

        var selectedId = gantt.getSelectedId();
        if (selectedId) {
            gantt.showLightbox(selectedId);
        }

    };

    this._doAllSlotSave = function() {
        that.convertTasksToSlots();
        var slots = that.getLightProfileSlotsFromGantt();
        var slots = that.convertSlotsToLightProfileSlots(slots);

        var lightProfile = that.lightProfiles[that.lightProfileId];
        lightProfile.slots = slots;




        that.LightProfileController.replaceLightProfileSlots(that.lightProfileId,slots,that.reloadLightProfileSlots);


        that.LightProfileController.replaceLightProfileSlots(that.lightProfileId,slots,that,that.reloadLightProfileSlots);

        //lightProfile.slots =
        //var json = that.lightProfiles[that.lightProfileId].getSlotsJson();
        //var loader = dhtmlxAjax.getSync(that.mod_slots+"?save_light_profiles_slots_json&light_profile="+that.dhxTree.getUserData(that.dhxTree.getSelectedItemId(), "light_profile_id")+"&json="+json);

    };


       this._doEditLightProfileWindow = function() {
        if (that.currentSelectedTreeModified) {
            alert("Save or revert configuration before editing  a light profile");
            that.dhxTree.selectItem(that.lightProfileId,false,false);
        }
        else {
            this.window_editslot = this.dhxWins.createWindow('window_editslot', 0, 0, 340, 220);
            var str = [
                { type:"hidden" , name:"id", value:that.dhxTree.getUserData(that.dhxTree.getSelectedItemId(), "light_profile_id") ,offsetLeft:"10", offsetTop:"10" },
                { type:"block" , name:"form_block_1",  list:[
                    { type:"input" , name:"name", label:"Name", value:that.dhxTree.getUserData(that.dhxTree.getSelectedItemId(), "name"), validate:"NotEmpty", labelWidth:110  },
                    { type:"input" , name:"description", value:that.dhxTree.getUserData(that.dhxTree.getSelectedItemId(), "description"), label:"Description", rows:"3", labelWidth:110  },
                    { type:"block" , name:"form_block_2", offsetLeft:"85", list:[
                        { type:"button" , name:"btn_edit", value:"Edit"  },
                        {type:"newcolumn"},
                        { type:"button" , name:"btn_cancel", value:"Cancel"  }
                    ]  }
                ]  }
            ];

            this.form_edit_light_profile = this.window_editslot.attachForm(str);
            this.form_edit_light_profile.attachEvent("onButtonClick", function(name) {
                if (name=="btn_edit") {
                    that.form_edit_light_profile.send(that.mod_slots+"?edit_light_profile", "post", function(loader, response){
                        that._reloadLightProfiles();
                        that.triggerUpdateLightProfiles();that.window_editslot.close();});
                }
                if (name=="btn_cancel") {
                    that.window_editslot.close();
                }

            });
            this.window_editslot.setText('Edit Light profile');
            this.window_editslot.denyResize();
            this.window_editslot.setModal(1);
            this.window_editslot.centerOnScreen();
            this.window_editslot.button('park').hide();
            this.window_editslot.button('minmax1').hide();

        }
    }



};


function LightProfileSlot(obj) {
    this._slot = -1;
    this.light_profile = -1;
    this.slot = -1;
    this.duration = 0;
    this.name = "";
    this.description = "";
    this._pw0 = 0;
    this._pw1 = 0;
    this._pw2 = 0;
    this._pw3 = 0;
    this.dayOn = 0;
    this.dayOff = 0;
    this.timeOn = 0;
    this.timeOff = 0;
    this.enabled = true;
    this.progress = 0;
    this.start_date = "";
    this.end_date = "";
    this.eas = 0;
    this.ecr = 0;
    this.emo = 0;
    this.id = -1;
    this.fadeIn = 10;
    this.fadeOut = 10;

    this.motionDuration = 10;
    this.motionDelay = 0;
    this.motionLightLevel = 0;
    this._mi0 = 0;
    this._mi1 = 0;
    this._mi2 = 0;
    this._mi3 = 0;
    this.motionFadeIn = 0;
    this.motionFadeOut = 0;

    this.getTask = function() {

    };

    Object.defineProperty(this, "pw0", { get: function () { return  parseInt(this._pw0); }, set: function(value) {try {this._pw0 = parseInt(value); this.progress = parseInt(value)/100;} catch(Exception) {this._pw0=0;} } });
    Object.defineProperty(this, "pw1", { get: function () { return  parseInt(this._pw1); }, set: function(value) {try {this._pw1 = parseInt(value);} catch(Exception) {this._pw1=0;} } });
    Object.defineProperty(this, "pw2", { get: function () { return  parseInt(this._pw2); }, set: function(value) {try {this._pw2 = parseInt(value);} catch(Exception) {this._pw2=0;} } });
    Object.defineProperty(this, "pw3", { get: function () { return  parseInt(this._pw3); }, set: function(value) {try {this._pw3 = parseInt(value);} catch(Exception) {this._pw3=0;} } });


    Object.defineProperty(this, "mi0", { get: function () { return  parseInt(this._mi0); }, set: function(value) {try {this._mi0 = parseInt(value); this.motionLightLevel = parseInt(value);} catch(Exception) {this._mi0=0;} } });
    Object.defineProperty(this, "mi1", { get: function () { return  parseInt(this._mi1); }, set: function(value) {try {this._mi1 = parseInt(value);} catch(Exception) {this._mi1=0;} } });
    Object.defineProperty(this, "mi2", { get: function () { return  parseInt(this._mi2); }, set: function(value) {try {this._mi2 = parseInt(value);} catch(Exception) {this._mi2=0;} } });
    Object.defineProperty(this, "mi3", { get: function () { return  parseInt(this._mi3); }, set: function(value) {try {this._mi3 = parseInt(value);} catch(Exception) {this._mi3=0;} } });


    Object.defineProperty(this, "slot", { get: function () { return  parseInt(this._slot); }, set: function(value) {try {this._slot = parseInt(value);} catch(Exception) {this._slot=-1;} } });
    //Object.defineProperty(this, "id", { get: function () { return  parseInt(this.slot); }, set: function(value) {this.slot = value;} });


    Object.defineProperty(this, "don", { get: function () { return  parseInt(this.dayOn); }, set: function(value) {
        try {
            this.dayOn=""+parseInt(value);
            if (isNaN(this.dayOn)) this.dayOn = 10;
        }
        catch(Exception) { this.dayOn = 10; }
        return;
        return;
        switch(value) {
            case 0: this.dayOn = new Date(2001, 0, 1, 00, 00); break;
            case 1: this.dayOn = new Date(2001, 0, 2, 00, 00); break;
            case 2: this.dayOn = new Date(2001, 0, 3, 00, 00); break;
            case 3: this.dayOn = new Date(2001, 0, 4, 00, 00); break;
            case 4: this.dayOn = new Date(2001, 0, 5, 00, 00); break;
            case 5: this.dayOn = new Date(2001, 0, 6, 00, 00); break;
            case 6: this.dayOn = new Date(2001, 0, 7, 00, 00); break;
            default: this.dayOn = new Date(2001, 0, 7, 00, 00); break;
        }
    } });

    Object.defineProperty(this, "dof", { get: function () { return  parseInt(this.dayOff); }, set: function(value) {
        try {
            this.dayOff=""+parseInt(value);
            if (isNaN(this.dayOff)) this.dayOff = 10;
        }
        catch(Exception) { this.dayOff = 10; }
        return;
        switch(value) {
            case 0: this.dayOff = new Date(2001, 0, 1, 00, 00); break;
            case 1: this.dayOff = new Date(2001, 0, 2, 00, 00); break;
            case 2: this.dayOff = new Date(2001, 0, 3, 00, 00); break;
            case 3: this.dayOff = new Date(2001, 0, 4, 00, 00); break;
            case 4: this.dayOff = new Date(2001, 0, 5, 00, 00); break;
            case 5: this.dayOff = new Date(2001, 0, 6, 00, 00); break;
            case 6: this.dayOff = new Date(2001, 0, 7, 00, 00); break;
            default: this.dayOff = new Date(2001, 0, 7, 00, 00); break;
        }
    } });

    Object.defineProperty(this, "dayOnDate", { get: function () {
        return new Date(2001, 0, 1, 00, 00);
        switch(this.dayOn) {
            case 0: return new Date(2001, 0, 1, 00, 00); break;
            case 1: return new Date(2001, 0, 2, 00, 00); break;
            case 2: return new Date(2001, 0, 3, 00, 00); break;
            case 3: return new Date(2001, 0, 4, 00, 00); break;
            case 4: return new Date(2001, 0, 5, 00, 00); break;
            case 5: return new Date(2001, 0, 6, 00, 00); break;
            case 6: return new Date(2001, 0, 7, 00, 00); break;
            default: return new Date(2001, 0, 7, 00, 00); break;
        }
    }});

    Object.defineProperty(this, "dayOffDate", { get: function () {
        switch(this.dayOff) {
            case 0: return new Date(2001, 0, 1, 00, 00); break;
            case 1: return new Date(2001, 0, 2, 00, 00); break;
            case 2: return new Date(2001, 0, 3, 00, 00); break;
            case 3: return new Date(2001, 0, 4, 00, 00); break;
            case 4: return new Date(2001, 0, 5, 00, 00); break;
            case 5: return new Date(2001, 0, 6, 00, 00); break;
            case 6: return new Date(2001, 0, 7, 00, 00); break;
            default: return new Date(2001, 0, 7, 00, 00); break;
        }
    }});



    Object.defineProperty(this, "ton", {
        get: function () {
            return formatDate(this.start_date,"HH:mm");
            //return  this.timeOn;
        },
        set: function(value) {
            try {
                var hours = value.split(":")[0];
                var minutes = value.split(":")[1];
                this.timeOn = new Date(2001, 0, 1, hours, minutes);
                this.start_date = new Date(2001, 0, 1, hours, minutes);
            }
            catch(Exception ) {
                this.timeOn = new Date(2001, 0, 1, 0, 0);
                this.start_date = new Date(2001, 0, 1, 0, 0);
            }
        }
    });

    Object.defineProperty(this, "tof", {
        get: function () {
            return formatDate(this.end_date,"HH:mm");
            //return  this.timeOff;
        },
        set: function(value) {
            try {
                var hours = value.split(":")[0];
                var minutes = value.split(":")[1];
                this.timeOff = new Date(2001, 0, 1, hours, minutes);
                this.end_date = new Date(2001, 0, 1, hours, minutes);

            }
            catch(Exception ) {
                this.timeOff = new Date(2001, 0, 1, 0, 0);
                this.end_date = new Date(2001, 0, 1, 0, 0);

            }
        }
    });

    Object.defineProperty(this, "TwilightEnabled", { get: function () { return  isTrue(this.ecr); }, set: function(value) {console.log(">SET TwilightEnabled task:"+this.id+"="+isTrue(value)); this.ecr = isTrue(value);} });
    Object.defineProperty(this, "AstroEnabled", { get: function () { return  isTrue(this.eas); }, set: function(value) {console.log(">SET AstroEnabled task:"+this.id+"="+isTrue(value)); this.eas = isTrue(value);} });
    Object.defineProperty(this, "MotionEnabled", { get: function () { return  isTrue(this.emo); }, set: function(value) {console.log(">SET MotionEnabled task:"+this.id+"="+isTrue(value)); this.emo = isTrue(value);} });

    /*
     Object.defineProperty(this, "start_date", {
     get: function () {
     console.log("GET id:" + this.id + " Start: " + this._startDate);
     return  this._startDate;
     },
     set: function(val) {
     console.log(">>SET id:" + this.id + " Start: " + val);

     this._startDate = val;
     }
     });

     Object.defineProperty(this, "end_date", {
     get: function () {
     console.log("GET id:" + this.id + " End: " + this._endDate);
     return  this._endDate;
     },
     set: function(value) {
     try {
     console.log(">>SET id:" + this.id + " End: " + value);
     this._endDate = value;
     }
     catch(Exception ) {
     console.log(Exception);
     this._endDate = new Date(2001, 0, 1, 23, 0);
     }
     } });*/

    Object.defineProperty(this, "text", { get: function () { return  this.name; }, set: function(value) { this.name = value; } });



    Object.defineProperty(this, "lightLevel", { get: function () { return  this.pw0; },
        set: function(value) {
            console.log(value);
            this.progress=value/100;
            this.pw0=value;
        } });


    this.initLightSlot = function() {
        if (this.don<=6) {
            this.start_date = new Date(2001, 0, 1 + this.don, this.start_date.getHours(), this.start_date.getMinutes());
            if (this.dof <= 6)
                this.end_date = new Date(2001, 0, 1 + this.dof, this.end_date.getHours(), this.end_date.getMinutes());
        }
        if (this.don>6) {
            if (this.start_date > this.end_date) {
                this.start_date = new Date(2001, 0, 1, this.start_date.getHours(), this.start_date.getMinutes());
                this.end_date = new Date(2001, 0, 2, this.end_date.getHours(), this.end_date.getMinutes());
            }
        }
    };

    this.calculateEndDate = function() {
        console.log(this.start_date);
        console.log(this.end_date);
        this.end_date = new Date(this.start_date.getFullYear(),this.start_date.getMonth(), this.start_date.getDate(), this.end_date.getHours(),this.end_date.getMinutes(),0,0);


        if(this.end_date<this.start_date) {
            //Over midnight
            if(this.dayOn<=6) {
                if (this.dayOff<=this.dayOn) this.dayOff = this.dayOn + 1;
                this.end_date.addDays(1);
            }
            else {
                //fix day off
                this.dayOff = this.dayOn;
                this.end_date.addDays(1);
            }
        }
        else {
            if(this.dayOn<=6) {
                if (this.dayOff>this.dayOn) this.end_date.addDays(1);
            }
        }
        this.duration = this.start_date.getMinutesToDate(this.end_date);
        console.log(this.end_date);
        console.log(this.duration);

    };

    this.getDict = function() {
        try {
            var result = {};
            result.id= this.id;
            result.light_profile= this.light_profile;
            result.slot= this.$index+1;
            result.name= this.name;
            result.description= this.description;
            result.don= this.don;
            result.ton= this.start_date.format("HH:MM");
            result.dof= this.dof;
            result.tof= this.end_date.format("HH:MM");
            result.pw0= this.lightLevel;
            result.pw1= this.pw1;
            result.pw2= this.pw2;
            result.pw3= this.pw3;
            result.eas= this.AstroEnabled;
            result.ecr= this.TwilightEnabled;
            result.emo= this.MotionEnabled;
            result.fadeIn= this.fadeIn;
            result.fadeOut= this.fadeOut;
            result.motionDelay=this.motionDelay;
            result.motionDuration=this.motionDuration;
            result.mi0=this.motionLightLevel;
            result.mi1=this.mi1;
            result.mi2=this.mi2;
            result.mi3=this.mi3;
            result.motionFadeIn= this.motionFadeIn;
            result.motionFadeOut= this.motionFadeOut;

            result.enabled= true;
            return result;
        }
        catch(Exception) {
            console.log(Exception);
            return {}
        }
    };


    // IF AN OBJECT WAS PASSED THEN INITIALISE PROPERTIES FROM THAT OBJECT
    for (var prop in obj) {
        if (this.hasOwnProperty(prop) || prop ==="pw0"|| prop ==="pw1"|| prop ==="pw2" || prop ==="pw3" || prop ==="don" || prop ==="dof" || prop ==="ton" || prop ==="tof" || prop ==="emo" || prop ==="ecr" || prop ==="eas" )
            this[prop] = obj[prop];
    }
    this.initLightSlot();


};

