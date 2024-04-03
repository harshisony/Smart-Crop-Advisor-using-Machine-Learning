<!DOCTYPE html>
<html>
<?php include ('header.php');  ?>

  <body class="bg-white" id="top">
  
  <?php
// Turn on error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

?>

<!DOCTYPE html>
<html>
<?php include ('header.php');  ?>

  <body class="bg-white" id="top">
  
<?php include ('nav.php');  ?>

 
  <section class="section section-shaped section-lg">
    <div class="shape shape-style-1 shape-primary">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
    </div>
<!-- ======================================================================================================================================== -->

<div class="container ">
    
         <div class="row">
          <div class="col-md-8 mx-auto text-center">
            <span class="badge badge-danger badge-pill mb-3">Prediction</span>
          </div>
        </div>
        
          <div class="row row-content">
            <div class="col-md-12 mb-3">

                <div class="card text-white bg-gradient-success mb-3">
                <form role="form" action="#" method="post" >  
                  <div class="card-header">
                  <span class=" text-info display-4" > Rainfall Prediction  </span>    
                  
                  </div>

                  <div class="card-body text-dark">
                     
                <table class="table table-striped table-hover table-bordered bg-gradient-white text-center display" id="myTable">

    <thead>
                    <tr class="font-weight-bold text-default">
                    <th><center>Region</center></th>
                    <th><center>Month</center></th>
                    <th><center>Prediction</center></th>
                    
                    
        </tr>
    </thead>
 <tbody>
                                 <tr class="text-center">

                                   <td>
                                        <div class="form-group ">
                                                <select id="region-select" name="region" class="form-control" required>
                                                    <option value="">Select Region</option>
                                                </select>
                                                <script language="javascript"> print_region("region-select"); </script>
                                        </div>
                                    </td>

                                    <td>
                                        <div class="form-group ">
                                                <select id="month-select" name="month" class="form-control" required>
                                                    <option value="">Select Month</option>
                                                </select>
                                                <script language="javascript"> print_months("month-select"); </script>
                                        </div>
                                    </td>
                                    
                                    <td>
                                    <center>
                                        <div class="form-group ">
                                            <button type="submit" value="Yield" name="Rainfall_Predict" class="btn btn-success btn-submit">Predict</button>
                                        </div>
                                    
                                    </center>
                                    </td>
                                </tr>
                            </tbody>
                            
                    
    </table>
    </div>
    </form>
</div>

<div class="card text-white bg-gradient-success mb-3">
                  <div class="card-header">
                  <span class=" text-success display-4" > Result  </span>                   
                  </div>

                    <h4>
                    <?php 
                    
                    
                    if(isset($_POST['Rainfall_Predict'])){
                        $region = $_POST['region'];
                        $month = $_POST['month'];

                        // Validate input
                        if(empty($region) || empty($month)) {
                            echo "Please select both region and month.";
                        } else {
                            // Escape user inputs to prevent shell injection
                            $Jregion = escapeshellarg($region);
                            $Jmonth = escapeshellarg($month);

                            // Execute the Python script
                            $command = "python ML/rainfall_prediction/rainfall_prediction.py $Jregion $Jmonth 2>&1";
                            $output = shell_exec($command);

                            // Display the output or error message
                            if($output === null) {
                                echo "Error occurred while executing the script.";
                            } else {
                                echo "Predicted Rainfall for  Region $region in the month $month is (in mm): $output";
                            }
                        }
                    }
                    ?>
                    </h4>
            </div>
 
    
    
            </div>
          </div>  
       </div>
         
</section>

    <?php require("footer.php");?>

</body>
</html>

					</h4>
            </div>
 
	
	
            </div>
          </div>  
       </div>
		 
</section>

    <?php require("footer.php");?>

</body>
</html>

