$.ready(
    $("button#btn-ajax").click(function() {
        $.post('/ajax/blog/right_back_at_you.json',
            {name:"Joe 赵 Stump",age:31},
            function(data) {
                // $("#jsonview").jsonView(data);
                var tmp = "<p>你好{data.name}。你今年<strong>{data.age}</strong>岁。</p>";
                $("#jsonview").append($.nano(tmp, data));
            });
    })
);