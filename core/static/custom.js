// // Form resetleme
$('#matModal').on('hidden.bs.modal', function (e) {
    $('#formMat').trigger("reset");
});
//
// $('#diverterModal').on('hidden.bs.modal', function (e) {
//     $('#formDiverter').trigger("reset");
// });
//
// $('#rcpModal').on('hidden.bs.modal', function (e) {
//     $('#formRcp').trigger("reset");
// });
//
// $('#rcpInputModal').on('hidden.bs.modal', function (e) {
//     $('#formRcpInput').trigger("reset");
// });
//
// $('#rcpOutputModal').on('hidden.bs.modal', function (e) {
//     $('#formRcpOutput').trigger("reset");
// });

$('#productOrdModal').on('hidden.bs.modal', function (e) {
    $('#formProductOrd').trigger("reset");
});


$('#mixOrdModal').on('hidden.bs.modal', function (e) {
    $('#formMixOrd').trigger("reset");
});

//. Form resetleme


function check(id) {
    document.getElementById(id).checked = true;
}

function uncheck(id) {
    document.getElementById(id).checked = false;
}


function removeOptions(selectElement) {
   var i, L = selectElement.options.length - 1;
   for(i = L; i >= 0; i--) {
      selectElement.remove(i);
   }
}

// using the function:
  function DownloadFile(item) {
    //Set the File URL.
    var url = 'burakexcel.php?friend=111';
    var fileName = "xls-dosyasi-adi.xls";

    var buton = $(item);
    buton.button('loading');

    $.ajax({
        url: url,
        cache: false,
        xhr: function () {
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 2) {
                    if (xhr.status == 200) {
                        xhr.responseType = "blob";
                    } else {
                        xhr.responseType = "text";
                    }
                }
            };
            return xhr;
        },
        success: function (data) {
            try {
                //Convert the Byte Data to BLOB object.
                var blob = new Blob([data], { type: "application/octetstream" });

                //Check the Browser type and download the File.
                var isIE = false || !!document.documentMode;
                if (isIE) {
                    window.navigator.msSaveBlob(blob, fileName);
                } else {
                    var url = window.URL || window.webkitURL;
                    link = url.createObjectURL(blob);
                    var a = $("<a />");
                    a.attr("download", fileName);
                    a.attr("href", link);
                    $("body").append(a);
                    a[0].click();

                    buton.button('reset');
                }
            }
            catch(err) {

                alert("HATA!!!")
                console.log(err.message);
                buton.button('reset');
            }




        }
    });
};
