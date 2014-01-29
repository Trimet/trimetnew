// Generated by CoffeeScript 1.6.3
(function() {
  var sidemenu_ajax, sleep;

  sleep = function() {
    return true;
  };

  sidemenu_ajax = function(link) {
    $("#contents").fadeOut(400);
    return $.ajax({
      type: "GET",
      url: link.href,
      async: true,
      success: function(html) {
        $("#contents").html(html);
        $(".sidebar").find("li").each(function() {
          return $(this).removeClass("sm_active");
        });
        $(link).closest("li").addClass("sm_active");
        $("#contents").fadeIn(400);
        $(document).attr('title', link.title);
        return window.history.pushState('', '', link.href);
      }
    });
  };

  $(document).ready(function() {
    $(".sm_link").click(function() {
      return sidemenu_ajax(this);
    });
    return $(".mm_link").click(function() {
      var link;
      link = this;
      $("#Wrapper2").fadeOut(400);
      return $.ajax({
        type: "GET",
        url: this.href,
        async: true,
        success: function(html) {
          $("#Wrapper2").html(html);
          $(".navigation").find("a").each(function() {
            return $(this).removeClass("mm_active");
          });
          $(link).addClass("mm_active");
          $("#Wrapper2").fadeIn(400);
          $(document).attr('title', link.title);
          window.history.pushState('', '', link.href);
          return $(".sm_link").click(function() {
            return sidemenu_ajax(this);
          });
        }
      });
    });
  });

}).call(this);
