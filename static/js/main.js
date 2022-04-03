var $message = $("#message");
$message.on("keydown keypress", function() {    
    var $this = $(this),
        val = $(this).val()
                     .replace(/(\r\n|\n|\r)/gm," ") // replace line breaks with a space
                     .replace(/ +(?= )/g,''); // replace extra spaces with a single space

    $this.val(val);
    // console.log("space checking")
});

// on button click
$('#onsub').click(function (e) {
    e.preventDefault();
    console.log("onsub working")
    
    $("#overlay").fadeIn(300);

    
    
    var message = $("#message").val();

    fetch('/submit', {
      body: JSON.stringify({urls:message}),
      method: 'POST',
      headers: {
          'Content-Type': 'application/json; charset=utf-8'
      },
    })
    .then(response => response.blob())
    .then(response => {
        console.log('responce received')
        const blob = new Blob([response], {type: 'application/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'});
        const downloadUrl = URL.createObjectURL(blob);
        $('#dwnlod').css('display', 'block')
        $('#dwnlod').attr('href', downloadUrl);
        $('#dwnlod').attr('download','urls.xlsx');
        $("#overlay").fadeOut(300);
    })

     
  });



  //  sejda.com
  //  iitg.ac.in 
  //  facebook.com 
  //  medium.com