// Password is abc123

var SECRET = "abc123";

function start(){
    while (true){
        
        var password = readLine("Enter password: ");
        
        if (password == SECRET){
            
            var ACCESS_CODE = Randomizer.nextInt(10000, 99999);
            println("Access Code: " + ACCESS_CODE);
            println("You have been sent an access code. Enter the access code to gain entry.");
            
            while (true){
                var accessCode = readLine("Enter access code: ");
                if (accessCode == ACCESS_CODE){
                break;
                }
                println("Sorry, that did not match. Please try again.");
            }
            break;
        }
        println("Sorry, that did not match. Please try again.");
    }

    println("You have logged in!");
}