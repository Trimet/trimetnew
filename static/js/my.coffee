sleep = () ->
    true

sidemenu_ajax = (link) ->
    $("#contents").fadeOut(400)

    $.ajax
        type: "GET"
        url: link.href
        async: true
        success: (html) ->

            $("#contents").html(html)
            $(".sidebar").find("li").each ->
                $(this).removeClass("sm_active")
            $(link).closest("li").addClass("sm_active")
            $("#contents").fadeIn(400)
            # $(document.title).html(link.title)
            # alert(link.title)
            $(document).attr('title', link.title)

            window.history.pushState(
                '',
                '',
                link.href
            )


$(document).ready ->

    $(".sm_link").click ->

        sidemenu_ajax(this)




    $(".mm_link").click ->
        # alert(this.href)
        link = this
        $("#Wrapper2").fadeOut(400)

        $.ajax
            type: "GET"
            url: this.href
            async: true
            success: (html) ->

                $("#Wrapper2").html(html)
                $(".navigation").find("a").each ->
                    $(this).removeClass("mm_active")
                $(link).addClass("mm_active")
                $("#Wrapper2").fadeIn(400)
                # $(document.title).html(link.title)
                $(document).attr('title', link.title)


                window.history.pushState(
                    '',
                    '',
                    link.href
                )

                $(".sm_link").click ->

                    sidemenu_ajax(this)