<?php

namespace FollowThroughWeb\Http\Controllers;

use Illuminate\Http\Request;

use FollowThroughWeb\User;
use Auth;

class UserController extends Controller
{
     /**
     * Api to get user information
     *
     * @return \Illuminate\Http\Response
     */
    public function user(Request $request)
    {
        //TODO: add encrypt and decrypt
        $email = $request->input('email');
        $password = $request->input('password');

        if (Auth::attempt(['email' => $email, 'password' => $password])) {
            $user = User::where('email','=',$email)->first();
            return response(array('userId'=>$user->id));
        } else {
            return response(array('userId'=>-1));
        }
    }
    
}
