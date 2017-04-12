@extends('layouts.app')

@section('content')
<!-- Page to display if the user has no shots -->
@if (is_null($shots))
<div>
    <h1 style="text-align: center; margin-top: 10%;"> Your account currently has no shots recorded </h1>
    <h3 style="text-align: center"> Use the FollowThrough- python app to record shots. The will be shown here </h3>
</div>
    
@else

<div class="mdl-grid">
    <div class="mdl-cell mdl-cell--1-col"></div>
    <div class="mdl-cell mdl-cell--4-col">

        <div class="avgStats">
            @foreach ($avgs[0] as $i=>$zone)
                @if ($i == 0)
                    @continue
                @endif
                <p>Zone {{$i}}: {{$zone}}% </p>
            @endforeach
            </br>
            </br>

            <p>Average Exit Angle: {{ $avgs[1] }}&deg;</p>
            <p>Average Entry Angle: {{ $avgs[2] }}&deg;</p>
            <p>Average Arc Height: {{ $avgs[3] }}m</p>
            <p>Average Shot Percentage: {{ $avgs[4] }}%</p>
        </div>
    
    </div>
    <div class="mdl-cell mdl-cell--6-col" style="overflow:auto; height: 80vh">
        <h3>Shots</h3>
        <table class="mdl-data-table mdl-js-data-table mdl-shadow--2dp" style="width:100%" >
            <thead>
                <tr>
                    <th>Zone</th>
                    <th class="mdl-data-table__cell--non-numberic">Over / Under</th>
                    <th>Exit Angle</th>
                    <th>Entry Angle</th>
                    <th>Arc Height</th>
                    <th>Made</th>
                </tr>
            </thead>
            <tbody>
                @foreach ($shots as $s)
                    <tr>
                        <td>{{ $s->zone }}</td>
                        @if ($s->over_under_shot == 'over')
                            <td class="mdl-data-table__cell--non-numberic">Over</td>
                        @else
                            <td class="mdl-data-table__cell--non-numberic">Under</td>
                        @endif
                        <td>{{ $s->exit_angle }}</td>
                        <td>{{ $s->entry_angle }}</td>
                        <td>{{ $s->arc_height }}</td>
                        @if ($s->made)
                            <td><i class="material-icons">check</i></td>
                        @else
                            <td><i class="material-icons">close</i></td>
                        @endif
                    </tr>
                @endforeach
           </tbody>
        </table>
    </div>

</div>
@endif
@endsection
