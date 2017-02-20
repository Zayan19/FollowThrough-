use Illuminate\Support\Facades\DB;

<?php

exec('python main.py',$python);
echo $python;
ob_start();
var_dump($python);
$result = ob_get_clean();
echo "\n";


if (preg_match_all('/"([^"]+)"/', $result, $m)) {
    $a = (String)($m[1][0]);
    $b = (String)($m[1][1]);
    $c = (String)($m[1][2]);
    $entryAngle = substr($a, strpos($a, ")"));
    echo "$entryAngle\n";

    $exitAngle = substr($b, strpos($b, ")"));
    echo "$exitAngle\n";


    $arcHeight = substr($c, strpos($c, ")"));
    echo "$arcHeight\n";
    /* echo gettype($a); */
    /* echo $m[2]; */
}

/* $myfile = fopen("data.txt", "a") or die("Unable to open file!"); */
/* fwrite($myfile, $entryAngle."\n"); */
/* fwrite($myfile, $exitAngle."\n"); */
/* fwrite($myfile, $arcHeight."\n"); */



?>
