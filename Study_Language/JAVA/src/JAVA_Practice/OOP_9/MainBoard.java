package JAVA_Practice.OOP_9;

public class MainBoard {

    public static void main(String[] args) {

        Player player = new Player();
        //lever 1
        player.play(1);

        AdvancedLevel aLevel = new AdvancedLevel();
        player.upgradeLevel(aLevel);
        player.play(2);

        SuperLevel sLevel = new SuperLevel();
        player.upgradeLevel(sLevel);
        player.play(3);

    }
}
