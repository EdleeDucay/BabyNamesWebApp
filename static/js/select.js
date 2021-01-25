
function select_action(select_id, value) {
    var select_id = document.getElementById(select_id);
    var input_box = document.querySelectorAll('.user-input')[0]
    var gender_input = document.querySelectorAll('.gender-input')[0]
    var year_input = document.querySelectorAll('.year-input')[0]
    var name_input = document.querySelectorAll('.name-input')[0]
    var name_input_wc = document.querySelectorAll('.name-input-wc')[0]
    var submit_btn = document.querySelectorAll('.submit-btn')[0]

    switch (value) {
        case "1":
            input_box.style.display = "block";
            gender_input.style.display = "block";
            year_input.style.display = "block";
            name_input.style.display = "none";
            name_input_wc.style.display = "none";        
            break;
        case "2":
            input_box.style.display = "block";
            gender_input.style.display = "none";
            year_input.style.display = "none";
            name_input.style.display = "block";
            name_input_wc.style.display = "none";
            break;
        case "3":
            input_box.style.display = "block";
            gender_input.style.display = "none";
            year_input.style.display = "block";
            name_input.style.display = "none";
            name_input_wc.style.display = "none";
            break;
        case "4":
            input_box.style.display = "block";
            gender_input.style.display = "none";
            year_input.style.display = "none";
            name_input.style.display = "none";
            name_input_wc.style.display = "none";
            break;
        case "5":
            input_box.style.display = "block";
            gender_input.style.display = "none";
            year_input.style.display = "none";
            name_input.style.display = "none";
            name_input_wc.style.display = "block";
            break;
        case "6":
            input_box.style.display = "block";
            gender_input.style.display = "none";
            year_input.style.display = "none";
            name_input.style.display = "none";
            name_input_wc.style.display = "none";
            break;
        default:
            input_box.style.display = "none";
            gender_input.style.display = "none";
            year_input.style.display = "none";
            name_input.style.display = "none";
            name_input_wc.style.display = "none";
            break;
    }
    
}