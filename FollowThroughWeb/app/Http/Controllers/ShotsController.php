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
            $user_id = Auth::user()->id;
            $shots = User::find($user_id)->shots;
            
            if ($shots->isEmpty()) {
                return view('shots')->with('shots', NULL);
            } else {
                $avgs = ShotsController::calcAvgs($shots);
                return view('shots')->with('shots', $shots)->with('avgs', $avgs);
            }

        } else {
            return view('forbidden');
        }
    }

    public function calcAvgs($shots)
    {
        // Compute Zone Averages

        $num_shots = count($shots);
        $zones_made = array_fill(0, 5, 0);
        $zones_total = array_fill(0, 5, 0);
        $zone_avg = array_fill(0, 5, 0);
        foreach ($shots as $i=>$s) {
            if ($s->made) {
                $zones_made[$s->zone] ++;
                $zones_total[$s->zone] ++;
            } else {
                $zones_total[$s->zone] ++;
            }
        }

        for ($i = 0; $i < count($zones_total); $i++) {
            if ($zones_total[$i] == 0) {
                $zone_avg[$i] = 0;
            } else {
                $zone_avg[$i] = ($zones_made[$i] / $zones_total[$i]) * 100;
            }
        }

        // Compute Average Angles
        $exit_avg = 0;
        foreach ($shots as $i=>$s) {
            $exit_avg += $s->exit_angle;
        }
        $exit_avg /= $num_shots;
        $exit_avg = round($exit_avg, 2);

        $entry_avg = 0;
        foreach ($shots as $i=>$s) {
            $entry_avg += $s->entry_angle;
        }
        $entry_avg /= $num_shots;
        $entry_avg = round($entry_avg, 2);


        // Compute Average Arc Height
        $arc_height_avg = 0;
        foreach ($shots as $i=>$s) {
            $arc_height_avg += $s->arc_height;
        }
        $arc_height_avg /= $num_shots;
        $arc_height_avg = round($arc_height_avg, 2);


        // Compute Average Shot Percentage
        $shots_avg = 0;
        foreach ($shots as $i=>$s) {
            if ($s->made) {
                $shots_avg ++;
            }
        }
        $shots_avg = ($shots_avg / $num_shots);
        $shots_avg = round($shots_avg, 2) * 100;


        return array($zone_avg, $exit_avg, $entry_avg, $arc_height_avg, $shots_avg);
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
