@extends('layouts.app')
@section('content')
<div class="mdl-grid" style="margin-top: 5%">
    <div class="mdl-cell mdl-cell--4-col"></div>
    <div class="mdl-cell mdl-cell--4-col mdl-shadow--2dp" style="display: inline-block; padding: 30px">
        <h2 style="text-align: center">Login</h2>
        <form role="form" method="POST" action="{{ route('login') }}">
            {{ csrf_field() }}

            <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label {{ $errors->has('email') ? 'is-invalid' : '' }}" style="margin-left: 23%">
                <input class="mdl-textfield__input" type="email" id="email" name="email" value="{{ old('email') }}" required autofocus>
                <label class="mdl-textfield__label" for="email">Email</label>
                @if ($errors->has('email'))
                    <span class="mdl-textfield__error">{{ $errors->first('email') }}</span>
                @endif
            </div>
            <div></div>
            <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label {{ $errors->has('email') ? 'is-invalid' : '' }}" style="margin-left: 23%">
                <input class="mdl-textfield__input" type="password" id="password" name="password" required>
                <label class="mdl-textfield__label" for="password">Password</label>
                @if ($errors->has('email'))
                    <span class="mdl-textfield__error">{{ $errors->first('password') }}</span>
                @endif
            </div>
            <div></div>
            <div style="margin-left: 25%">
                <label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="remember">
                    <input type="checkbox" id="remember" class="mdl-checkbox__input" name="remember" {{ old('remember') ? 'checked' : ''}} >
                    <span class="mdl-checkbox__label">Remember Me</span>
                </label>
            </div>
            <div></div>
            <div style="margin-top: 20px; margin-left: 23%;">
                <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored" type="submit" style="width: 70%">
                    Login
                </button>
            </div>
            <div style="margin-top: 30px; margin-left: 40%">
                <a href="{{ route('password.request') }}" style="color: #636b6f">
                    <button type="button" class="mdl-button mdl-js-button">
                        Forgot Your Password?
                    </button>
                </a>
            </div>
        </form>
    </div>
</div>

@endsection
