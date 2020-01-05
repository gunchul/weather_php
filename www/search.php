<?php
$now = new DateTime;
$search_date=$_POST["search_date"];
$region=$_POST["region"];

if ( strlen($search_date) == 0 || strlen($region) == 0 ) {
    $search_date = $now->format('Y-m-d');
    $search_year = $now->format('Y');
    $region = "newcastle";
}
else {
    $search_year = sprintf("%.4s", $search_date);
}

$cmd = sprintf("cat data/%s/%s_%s.txt", $search_year, $search_date, $region);
$output = shell_exec($cmd);
if ($output == NULL)
{
   $output = sprintf("No data(%s)", $cmd);
}
?>

<!DOCTYPE html>
<html lang="ko">
<head>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-155280384-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-155280384-1');
</script>
<title>Search Weather</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  <style>
    pre {
      font-family: monospace;
    } 
</style>
</head>

<body>
<p>
<form action="search.php" id="search" method="post">
  지역: 
  <div class="btn-group">
    <?php
    $regions = array("boat_harbour"=>"보트하버", 
                 "newcastle"=>"뉴카슬", 
                 "frazer_beach"=>"프레이져비치",
                 "bondi"=>"시드니",
                 "wollongong"=>"울릉공",
                );

    foreach($regions as $key => $value) {
      if ($region == $key)
      {
        $active = " active";
      }
      else
      {
        $active = "";
      }

      echo '<button type="button" class="btn btn-primary' . $active . '" onclick="submit_by_region(\'' . $key . '\')" checked>' . $value . '</button>';
    }
    ?>
    <!-- <button type="button" class="btn btn-primary" onclick="submit_by_region('boat_harbour')">보트하버</button>
    <button type="button" class="btn btn-primary" onclick="submit_by_region('newcastle')">뉴카슬</button>
    <button type="button" class="btn btn-primary" onclick="submit_by_region('frazer_beach')">프레이져비치</button>
    <button type="button" class="btn btn-primary" onclick="submit_by_region('bondi')">시드니</button>
    <button type="button" class="btn btn-primary" onclick="submit_by_region('wollongong')">울릉공</button> -->
  </div>
  <br><br>                         
  날짜:
  <input type="date" value="<?php echo $search_date ?>" name="search_date" onchange="submit()">
  <br><br>
  <input type="hidden" id="region" name="region" value="<?php echo $region?>">
</form>
<br>
<div class="form-group">
  <label for="result">날씨:</label>
  <pre>
  <?php echo $output;?>
  </pre>
  <!-- <textarea style="font-family:consolas" class="form-control" rows="120" id="comment"><?php /*echo $output;*/?></textarea> -->
</div>

<script>
function submit_by_region(region) {
  document.getElementById("region").value = region;
  document.getElementById("search").submit();
}
</script>
</body>
</html>
