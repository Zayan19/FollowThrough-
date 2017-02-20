<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateShotsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('shots', function (Blueprint $table) {
            $table->increments('id');
	    $table->integer('user_id')->unsigned();
	    $table->timestamp('time_of_shot');
	    $table->integer('zone');
	    $table->string('over_under_shot', 10);
	    $table->decimal('exit_angle',5,2);
	    $table->decimal('entry_angle',5,2);
	    $table->decimal('arc_height',5,2);
	    $table->boolean('made');

            $table->timestamps();
	    $table->foreign('user_id')
		  ->references('id')->on('users')
  		  ->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('shots');
    }
}
