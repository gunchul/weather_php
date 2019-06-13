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
   $output = sprintf("No data");
}
?>

<!DOCTYPE html>
<html lang="ko">
<title>Search Weather</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<body>
<p>
<form action="search.php" method="post">
  지역: 
  <div class="btn-group" data-toggle="buttons">
    <label class="btn btn-primary">
      <input type="radio" id="newcastle" name="region" value="newcastle" 
      <?php 
          if (strcmp($region, "newcastle")==0)
          {
              echo " checked=\"checked\" autofocus=\"true\"";
          }
      ?> /> 뉴카슬
    </label>
    <label class="btn btn-primary">
      <input type="radio" id="bondi" name="region" value="bondi" 
      <?php 
          if (strcmp($region, "bondi")==0)
          {
              echo " checked=\"checked\" autofocus=\"true\"";
          }
      ?> /> 시드니
    </label>
    <label class="btn btn-primary">
      <input type="radio" id="wollongong" name="region" value="wollongong" 
      <?php 
          if (strcmp($region, "wollongong")==0)
          {
              echo " checked=\"checked\" autofocus=\"true\"";
          }
      ?>
      /> 울릉공
    </label>
  </div>
  <br><br>                         
  날짜:
  <input type="date" value="<?php echo $search_date ?>" name="search_date">
  <br><br>
  <button type="submit" class="btn btn-primary"> 검색 </button>
</form>
<br>
<div class="form-group">
  <label for="result">날씨:</label>
  <textarea style="font-family:consolas" class="form-control" rows="120" id="comment"><?php echo $output;?></textarea>
</div>
</body>
</html>
