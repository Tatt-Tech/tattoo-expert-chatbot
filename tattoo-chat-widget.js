function injectChatWidget() {
    // Inject CSS
    var css = `
        .chat-widget {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 350px;
            display: none;
            border-radius: 20px;
        }
        .chat-content {
          background-color: #f1f1f1;
          padding: 25px;
          border-radius: 20px;
          display: flex;
          flex-direction: column;
          position: relative;
      }
        .tattoo-icon {
            width: 50px;
            height: 50px;
            background-color: #38afdd;
            position: fixed;
            bottom: 20px;
            right: 20px;
            cursor: pointer;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .avatar-icon {
          width: 50px;
          height: 50px;
          background-color: white;
          border-radius: 50%;
          display: flex;
          justify-content: center;
          align-items: center;
          margin-right: 15px;
          flex-shrink: 0;
          position: absolute; 
          top: 10px; 
          left: 10px; 
      }  

      .avatar-icon img {
          width: 24px;
          height: 24px; 
      }
      
        .buttons-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 15px;
            margin-top: 15px;
        }
        .chat-widget .chatbot-message {
          display: flex;
          align-items: center;
        }
        
        .chat-widget .chatbot-message img {
          height: 30px;
        }
        .chat-widget .chatbot-message {
          display: flex;
          align-items: center;
          margin-bottom: 20px;
        }
        
        .chat-widget .chatbot-message img {
          height: 30px;
        }

        .loading-dots {
          display: inline-block;
          width: 20px;
          font-size: 14px;
          line-height: 1;
          animation: loadingDots 1s infinite;
        }
        
        @keyframes loadingDots {
          0%, 20% {
            color: rgba(0,0,0,0);
            text-shadow:
              .25em 0 0 rgba(0,0,0,0),
              .5em 0 0 rgba(0,0,0,0);}
          40% {
            color: black;
            text-shadow:
              .25em 0 0 rgba(0,0,0,0),
              .5em 0 0 rgba(0,0,0,0);}
          60% {
            text-shadow:
              .25em 0 0 black,
              .5em 0 0 rgba(0,0,0,0);}
          80%, 100% {
            text-shadow:
              .25em 0 0 black,
              .5em 0 0 black;}
        }
         .link {
          text-align: center; 
          margin-top: 15px;
          font-size: 12px;
         } 

         .logo {
          width: 75px;
        }

        .open_logo {
          width: 75px;
          margin-left: 5px;
        }

        .chat-messages {
          max-height: 300px;
          overflow-y: auto;
          padding-right: 10px;
          padding-left: 50px;
          margin-bottom: 15px;
        }        
    `;
    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);
  
    // Inject HTML
    var html = `
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Personal Tattoo Expert</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<div class="tattoo-icon">
    <img src="https://irp.cdn-website.com/dfaf08d8/dms3rep/multi/tattoo-machine-1.svg" alt="Tattoo Gun Icon" style="width: 24px; height: 24px;">
</div>

<div class="chat-widget">
  <div class="chat-content">
    <div class="chat-messages">
      <div class="chatbot-message" id="initial-message">
        <div>
            <div id="initial-message-text"></div>
        </div>
      </div>    
        <div id="chatbot-avatar">
          <div class="avatar-icon">
            <img src="https://irp.cdn-website.com/dfaf08d8/dms3rep/multi/robot.svg" alt="Avatar Icon">
          </div>
         </div> 
      <div id="chatbot-answer"></div>
      </div>
      <textarea id="message" class="form-control" rows="1" style="resize: none; margin-top: 50px;" placeholder="Ask a question..."></textarea>
      <div class="buttons-container">
          <button id="send" class="btn btn-primary mt-2" style="background-color: #38afdd; border: none;">Send</button>
          <button id="clear" class="btn btn-secondary mt-2">Clear</button>
      </div>
      <div class="link">
        <p>Powered by <a href="https://www.tatt-tech.com/" target="_blank"><img src="https://irp.cdn-website.com/dfaf08d8/dms3rep/multi/tatt-tech-high-resolution-logo-color-on-transparent-background.png" alt="Tatt Tech" class="logo"></a> x <a href="https://www.openai.com/"><img src="https://irp.cdn-website.com/dfaf08d8/dms3rep/multi/OpenAI_Logo.svg.png" alt="OpenAI" class="open_logo"></a></p>
    </div>    
  </div>
</div>
</body>
</html>

    `;
    var div = document.createElement('div');
    div.innerHTML = html;
    document.body.appendChild(div);
  }
  
  injectChatWidget();
  


function typeWriter(elementId, text, speed) {
    var i = 0;

    function typingAnimation() {
        if (i < text.length) {
            document.getElementById(elementId).innerHTML += text.charAt(i);
            i++;
            setTimeout(typingAnimation, speed);
        }
    }

    typingAnimation();
}

$(document).ready(function () {
  typeWriter("initial-message-text", "Hi, I'm Aurora, your personal tattoo expert!\n\nAnything I can help with? 😊", 50);

  $(".tattoo-icon").click(function () {
      $(".chat-widget").toggle();
      $(".tattoo-icon").toggle();
  });

  $(".chat-content").click(function () {
      event.stopPropagation();
  });

  $("#send").click(function () {
      var message = $("#message").val();
      if (message.trim() === "") {
          return;
      }
      $("#initial-message").hide(); // Hide the initial message

      // Add loading animation
      $(".chat-messages").append('<span class="loading-dots">...</span>');

      $.ajax({
          url: "https://tattoo-expert.herokuapp.com/",
          type: "POST",
          contentType: "application/json",
          data: JSON.stringify({ "message": message }),
          success: function (data) {
              $(".loading-dots").remove(); // Remove loading animation

              var responseHtml = '<div class="chatbot-message">' +
                                     '<div class="avatar-icon">' +
                                         '<img src="https://irp.cdn-website.com/dfaf08d8/dms3rep/multi/robot.svg" alt="Avatar Icon">' +
                                     '</div>' +
                                     '<div id="response-text"></div>' +
                                 '</div>';

              $(".chat-messages").append(responseHtml); // Show the response container next to the avatar-icon

              // Call the typeWriter function with the response text
              typeWriter("response-text", data.answer, 50);

              // Clear the question input and set the focus back to it
              $("#message").val("").focus();
          }
      });
  });

  $("#clear").click(function () {
      $(".chat-messages").html("");
      $("#message").val("");
      $("#initial-message").show(); // Show the initial message
  });
});