<?php
session_start();

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Collect username from the form
    $username = isset($_POST['username']) ? $_POST['username'] : '';

    // Validate the username (You may add more validation as needed)
    if (!empty($username)) {
        // Store the username in the session
        $_SESSION['username'] = $username;

        // Redirect to a secure page or perform further actions
        header('Location: welcome.php');
        exit;
    } else {
        // Display an error message if the username is empty
        $error = "Please enter a username.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>

    <h2>Login</h2>

    <?php
    // Display error message if exists
    if (isset($error)) {
        echo '<p style="color: red;">' . $error . '</p>';
    }
    ?>

    <form method="post" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <button type="submit">Login</button>
    </form>

</body>
</html>
