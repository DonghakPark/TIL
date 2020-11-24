package Design_Pattern.ch1;

public class MuteQuack implements QuackBehavior {
    public void quack(){
        System.out.println("<< ~ mute ~ >> ");
    }
}
