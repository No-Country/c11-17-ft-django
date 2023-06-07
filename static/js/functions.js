function submitServiceRequest(button) {
    var selectedDog = document.querySelector('#selectedDog').value;
    var startDate = document.querySelector('#startDate').value;
    var endDate = document.querySelector('#endDate').value;
    var postID = button.getAttribute('data-post-id');
  
    $.ajax({
        type: 'POST',
        url: '/reservations/request_service/' + postID + '/',
        data: {
            'dog': selectedDog,
            'start_date': startDate,
            'end_date': endDate,
            'csrfmiddlewaretoken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
        },
        success: function(response) {
            if (response.redirect_url) {
                window.location.href = response.redirect_url;
            }
        },
        error: function(response) {
            console.log(response);
        }
    });
  }
  