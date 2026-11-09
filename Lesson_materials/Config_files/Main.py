import config
def main():
    print(f"Welcome to {GAME_TITLE}!")

    player_health = config.PLAYER_HEALTH
    enemy_health = config.ENEMY_HEALTH

    while player_health > 0 and enemy_health > 0:
        print(f"\nPlayer Health: {player_health}")
        print(f"Enemy Health: {enemy_health}")

        action = input("Press Enter to attack or Q to quit: ")

        if action.lower() == "q":
            break

        enemy_health -= config.PLAYER_DAMAGE
        print(f"You dealt {config.PLAYER_DAMAGE} damage!")

        if enemy_health <= 0:
            print("You defeated the enemy!")
            break

        player_health -= config.ENEMY_DAMAGE
        print(f"The enemy dealt {config.ENEMY_DAMAGE} damage!")

    if player_health <= 0:
        print("Game Over!")


if __name__ == "__main__":
    main()