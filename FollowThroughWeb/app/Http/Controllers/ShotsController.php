<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use Illuminate\Database\Eloquent\ModelNotFoundException;

use App\Shots;
use App\User;
use Auth;

class ShotsController extends Controller
{
    /**
     * Display all the shots of the current user.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        if (Auth::check()) {
            //TODO: return a view 
            $user_id = Auth::user()->id;
            $shots = User::find($user_id)->shots;

            return response(array(
                'shots' => $shots->toArray()
            ), 200);
        } else {
            //TODO: return a view styll
            return response(array('error'=> $user_id),200);
        }
    }

    /**
     * Api to get the shot information of a requested user
     *
     * @return \Illuminate\Http\Response
     */
    public function index_api($id)
    {
        $user = User::find($id);
        if (is_null($user)) {
            return response(array('error'=>'user not found'));
        }

        $shots = $user->shots;
        return response(array('shots' => $shots));


        
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        if (empty ($request->user_id)) {
            return response(array('error' => 'Must provide user identification'));
        }

        $user_id = intval($request->user_id);
        $user = User::find($user_id);
        if (is_null($user)) {
            return response(array('error'=>'user not found'));
        }
        $shot = new Shots;
        //TODO: Make sure all parameters made it through!

        $shot->zone = intval($request->zone);
        $shot->over_under_shot = $request->over_under_shot;
        $shot->exit_angle = floatval($request->exit_angle);
        $shot->entry_angle = floatval($request->entry_angle);
        $shot->arc_height = floatval($request->arc_height);
        $shot->made = $request->made == "True" ? true :  false;
        $shot->time_of_shot = date("Y-m-d H:i:s");

        $user->shots()->save($shot);
        
        //Shots::create($request->all());
        return response(array('message'=>'Shot created successfully'));
    }

    /**
     * Display data about a specific shot!
     *
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
