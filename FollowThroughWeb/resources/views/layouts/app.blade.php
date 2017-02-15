<!DOCTYPE html>
<html lang="{{ config('app.locale') }}">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <title>{{ config('app.name') }}</title>
    <!-- MDL --> 
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.deep_orange-light_blue.min.css" /> 
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <!-- Custom Styles -->
    <link href="/css/app.css" rel="stylesheet">

    <!-- Scripts -->
<script>
window.Laravel = {!! json_encode([
    'csrfToken' => csrf_token(),
        ]) !!};
</script>
</head>
<body>
    <div class="mdl-layout mdl-js-layout" id="app">
      <header class="mdl-layout__header mdl-layout__header--scroll">
        <div class="mdl-layout__header-row">
          <span class="mdl-layout-title"><a class="brand" href="{{ url('/') }}">{{ config('app.name') }}</a></span>
          <!-- Add spacer, to align navigation to the right -->
          <div class="mdl-layout-spacer"></div>

            @if(Auth::check())
                <nav class="mdl-navigation">
                    <button id="logout-menu"
                            class="mdl-button mdl-js-button mdl-button--icon">
                      <i class="material-icons">more_vert</i>
                    </button>

                    <ul class="mdl-menu mdl-menu--bottom-left mdl-js-menu mdl-js-ripple-effect"
                        for="logout-menu">
                      <li class="mdl-menu__item">
                        <a href="{{ route('logout') }}" 
                           onclick="event.preventDefault();
                                    document.getElementById('logout-form').submit();">
                            Logout
                        </a>
                        <form id="logout-form" 
                              action="{{ route('logout') }}" 
                              method="POST" 
                              style="display: none;">
                            {{ csrf_field() }}
                        </form>
                      </li>
                    </ul>
                    {{ Auth::user()->name }}
                </nav>
            @endif
        </div>
      </header>
      <main class="mdl-layout__content">
        <div class="page-content">@yield('content')</div>
      </main>
    </div>

    <!-- Scripts -->
    <script src="/js/app.js"></script>
    <!-- MDL -->
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
</body>
</html>
