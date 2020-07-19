var db = firebase.firestore();

function send() {
    const gender = document.querySelector("#select1").value;
    const agetxt = document.querySelector("#age").value;
    const select2txt = document.querySelector("#select2").value;
    const cigtxt = document.querySelector("#cig").value;
    const address2txt = document.querySelector("#address2").value;
    const select3txt = document.querySelector("#select3").value;
    const select4txt = document.querySelector("#select4").value;
    const select5txt = document.querySelector("#select5").value;
    const choltxt = document.querySelector("#chol").value;
    const pretxt = document.querySelector("#pre").value;
    const dbltxt = document.querySelector("#dbl").value;
    const bmitxt = document.querySelector("#bmi").value;
    const hrttxt = document.querySelector("#hrt").value;
    const glutxt = document.querySelector("#glu").value;

    db.collection("features").doc().set({
            Gender: gender,
            Age: agetxt,
            currentsmoker: select2txt,
            CigarettesPerDay: cigtxt,
            BloodPressure: address2txt,
            prevalentStroke: select3txt,
            prevalentHyp: select4txt,
            diabetes: select5txt,
            totChol: choltxt,
            sysBP: pretxt,
            DiastolicBlood: dbltxt,
            BodyMassIndex: bmitxt,
            heartRate: hrttxt,
            glucose: glutxt

        })
        .then(function() {
            alert("Data added");
        })
        .catch(function(error) {
            alert("Error written document", error);

        });

}
