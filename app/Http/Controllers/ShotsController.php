<?php

namespace FollowThroughWeb\Http\Controllers;
use Illuminate\Http\Request;
use Illuminate\Database\Eloquent\ModelNotFoundException;

use FollowThroughWeb\Shots;
use FollowThroughWeb\User;
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
        Shots::create($request->all());
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
