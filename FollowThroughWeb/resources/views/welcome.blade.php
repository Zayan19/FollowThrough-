<!DOCTYPE html>
<html lang="{{ config('app.locale') }}">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>FollowThrough-</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,600" rel="stylesheet">
        <!-- Styles -->
        <style>
            html, body {
                background-color: #fff;
                color: #636b6f;
                font-family: 'Open Sans', sans-serif;
                font-weight: 300;
                font-size: 1em;
                height: 100vh;
                margin: 0;
            }

            .full-height {
                height: 100vh;
            }

            .flex-center {
                align-items: center;
                display: flex;
                justify-content: center;
            }

            .position-ref {
                position: relative;
            }

            .top-right {
                position: absolute;
                right: 10px;
                top: 18px;
            }

            .content {
                margin-top: -5%;
            }

            .welcome {
                text-align: center;
                font-size: 2em;
            }

            .title {
                text-align: center;
                font-size: 5em;
            }

            .links > a {
                color: #636b6f;
                padding: 0 25px;
                font-size: 12px;
                font-weight: 600;
                letter-spacing: .1rem;
                text-decoration: none;
                text-transform: uppercase;
            }

            .upsidedown {
                display: inline-block;
                -webkit-transform: rotateX(180deg);
                transform: rotateX(180deg); 
            }

            .svg_container {
                margin-bottom: -95px;
            }
            .ball_svg {
                margin-left: -25px
            }

            .bigF {
                display: inline-block;
                transform:scale(1,2.7) translate(0,-18px) rotate(-15deg);
            }

        </style>
    </head>
    <body>
        <div class="flex-center full-height">
                <div class="top-right links">
                    @if (Auth::check())
                        <a href="{{ url('/shots') }}">Home</a>
                    @else
                        <a href="{{ url('/login') }}">Login</a>
                        <a href="{{ url('/register') }}">Register</a>
                    @endif
                </div>

            <div class="content">
                <div class="svg_container">
                    <svg xmlns="http://www.w3.org/2000/svg" 
                         viewBox="0 0 575.00001 300" 
                         height="300" 
                         width="535">
                         <path d="M20 151s291-400 540 137" 
                               fill="none" 
                               stroke="#000" 
                               stroke-dasharray="4,8"/>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 49.999997 49.999997" 
                         class="ball_svg" height="25" width="25">
                        <g transform="translate(0 -1002.362)" fill="none" stroke="#000">
                            <ellipse ry="24.667" rx="24.417" cy="1027.495" cx="25.117"/>
                            <path d="M.566 1027.88c0-.07 9.765-25.51 47.692-9.2M9.623 
                                    1008.633s-8.915 39.484 26.18 40.474M29.153 1003.255s-46.135
                                    12.03 18.397 33.116M2.547 1018.54s.283 16.84 7.076 28.303"/>
                        </g>
                    </svg>
                </div>
                <div class="welcome">Welcome to</div>
                <div class="title">
                   <span class="bigF">&#6508;</span>ollowThroug<span class="">h</span>&#8210;
                </div>
            </div>
        </div>
    </body>
</html>
