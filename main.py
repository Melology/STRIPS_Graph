import networkx as nx
import matplotlib.pyplot as plt

# Creating Directed Graph Objects
G = nx.DiGraph()

# Nodes
G.add_node(1, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(2, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(3, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(4, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(5, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(6, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(7, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])


G.add_node(8, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(9, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(10, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(11, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(12, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(13, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(14, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(15, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(16, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(17, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(18, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(19, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(20, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(21, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(22, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(23, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(24, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(25, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(26, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(27, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(28, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(29, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(30, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(31, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(32, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(33, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(34, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(35, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])



G.add_node(36, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(37, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(38, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(39, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(40, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(41, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(42, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(43, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(44, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(45, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(46, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(47, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(48, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])


G.add_node(49, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(50, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(51, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(52, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(53, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: false",
        "i_am_in_healing_area: false",
        "i_found_enemy: false", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(53, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(54, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(55, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(56, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(57, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(58, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(59, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(60, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(61, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(62, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(63, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(64, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(65, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(66, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(67, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(68, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(69, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(70, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(71, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(72, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(73, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(74, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(75, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(76, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(77, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(78, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(79, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(80, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(81, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(82, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(83, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(84, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(85, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(86, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(87, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(88, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(89, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])


G.add_node(90, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(91, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(92, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(93, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(94, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: fasle",
        "enemy_is_dead: true",
        "friend_hp_is_low: true", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: true", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(95, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(96, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(97, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(98, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(99, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(100, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(101, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(102, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(103, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(104, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(105, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(106, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(107, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(108, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(109, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(110, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(111, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(112, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(113, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(114, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(115, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(116, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(117, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(118, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])


G.add_node(119, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(120, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(121, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(122, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])


G.add_node(123, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(124, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(125, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: false",
        "friend_is_dead: true",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(126, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(127, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(128, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: true", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])


G.add_node(129, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(130, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(131, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: true",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(132, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(133, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(134, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: true", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(135, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(136, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(137, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: true",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(138, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: fasle",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(139, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(140, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: true",
        "enemy_is_dead: false",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: true", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: true", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: true",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])


G.add_node(141, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(142, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(143, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: true", "my_defense_is_buffed: false", "my_speed_is_buffed: false"])

G.add_node(144, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(145, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(146, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: true", "my_speed_is_buffed: false"])

G.add_node(147, labels=[
        "enemy_attack_is_debuffed: true", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])


G.add_node(148, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: true",
        "enemy_speed_is_debuffed: false",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "  friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

G.add_node(149, labels=[
        "enemy_attack_is_debuffed: false", "enemy_defense_is_debuffed: false",
        "enemy_speed_is_debuffed: true",
        "enemy_hp_is_low: false", "enemy_hp_is_mid: false", "enemy_hp_is_high: false",
        "enemy_is_dead: true",
        "friend_hp_is_low: false", "friend_hp_is_mid: false", "friend_hp_is_high: true",
        "friend_is_dead: false",
        "friend_attack_is_buffed: false", "friend_defense_is_buffed: false", "friend_speed_is_buffed: false",
        "i_am_close_to_enemy: false", "i_am_close_to_friend: true",
        "i_am_in_healing_area: false",
        "i_found_enemy: true", "i_found_friend: true", "i_found_item: false",
        "i_have_power_portion: false",
        "i_have_mp_portion: true", "i_have_mp_for_debuff: false", "i_have_mp_for_fireball: false",
        "i_have_mp_for_heal: false", "i_have_mp_for_buff: false",
        "my_hp_is_low: false", "my_hp_is_mid: false", "my_hp_is_high: true",
        "my_attack_is_buffed: false", "my_defense_is_buffed: false", "my_speed_is_buffed: true"])

# Edges
G.add_edge(1, 2, label="buff_friend_defense")
G.add_edge(1, 3, label="buff_friend_speed")
G.add_edge(1, 4, label="buff_friend_attack")
G.add_edge(1, 5, label="buff_my_attack")
G.add_edge(1, 6, label="buff_my_defense")
G.add_edge(1, 7, label="buff_my_speed")

G.add_edge(1, 8, label="move_to_enemy")
G.add_edge(2, 9, label="move_to_enemy")
G.add_edge(3, 10, label="move_to_enemy")
G.add_edge(4, 11, label="move_to_enemy")
G.add_edge(5, 12, label="move_to_enemy")
G.add_edge(6, 13, label="move_to_enemy")
G.add_edge(7, 14, label="move_to_enemy")

G.add_edge(8, 15, label="debuff_enemy_attack")
G.add_edge(8, 16, label="debuff_enemy_defense")
G.add_edge(8, 17, label="debuff_enemy_speed")

G.add_edge(9, 18, label="debuff_enemy_attack")
G.add_edge(9, 19, label="debuff_enemy_defense")
G.add_edge(9, 20, label="debuff_enemy_speed")

G.add_edge(10, 21, label="debuff_enemy_attack")
G.add_edge(10, 22, label="debuff_enemy_defense")
G.add_edge(10, 23, label="debuff_enemy_speed")

G.add_edge(11, 24, label="debuff_enemy_attack")
G.add_edge(11, 25, label="debuff_enemy_defense")
G.add_edge(11, 26, label="debuff_enemy_speed")

G.add_edge(12, 27, label="debuff_enemy_attack")
G.add_edge(12, 28, label="debuff_enemy_defense")
G.add_edge(12, 29, label="debuff_enemy_speed")

G.add_edge(13, 30, label="debuff_enemy_attack")
G.add_edge(13, 31, label="debuff_enemy_defense")
G.add_edge(13, 32, label="debuff_enemy_speed")

G.add_edge(14, 33, label="debuff_enemy_attack")
G.add_edge(14, 34, label="debuff_enemy_defense")
G.add_edge(14, 35, label="debuff_enemy_speed")

G.add_edge(15, 53, label="move_to_friend")
G.add_edge(16, 54, label="move_to_friend")
G.add_edge(17, 55, label="move_to_friend")
G.add_edge(18, 56, label="move_to_friend")
G.add_edge(19, 57, label="move_to_friend")
G.add_edge(20, 58, label="move_to_friend")
G.add_edge(21, 59, label="move_to_friend")
G.add_edge(22, 60, label="move_to_friend")
G.add_edge(23, 61, label="move_to_friend")
G.add_edge(24, 62, label="move_to_friend")
G.add_edge(25, 63, label="move_to_friend")
G.add_edge(26, 64, label="move_to_friend")
G.add_edge(27, 65, label="move_to_friend")
G.add_edge(28, 66, label="move_to_friend")
G.add_edge(29, 67, label="move_to_friend")
G.add_edge(30, 68, label="move_to_friend")
G.add_edge(31, 69, label="move_to_friend")
G.add_edge(32, 70, label="move_to_friend")
G.add_edge(33, 71, label="move_to_friend")
G.add_edge(34, 72, label="move_to_friend")
G.add_edge(35, 73, label="move_to_friend")

G.add_edge(1, 36, label="fireball_enemy")
G.add_edge(2, 37, label="fireball_enemy")
G.add_edge(3, 38, label="fireball_enemy")
G.add_edge(4, 39, label="fireball_enemy")
G.add_edge(5, 40, label="fireball_enemy")
G.add_edge(6, 41, label="fireball_enemy")
G.add_edge(7, 42, label="fireball_enemy")
G.add_edge(53, 74, label="fireball_enemy")
G.add_edge(54, 75, label="fireball_enemy")
G.add_edge(55, 76, label="fireball_enemy")
G.add_edge(56, 77, label="fireball_enemy")
G.add_edge(57, 78, label="fireball_enemy")
G.add_edge(58, 79, label="fireball_enemy")
G.add_edge(59, 80, label="fireball_enemy")
G.add_edge(60, 81, label="fireball_enemy")
G.add_edge(61, 82, label="fireball_enemy")
G.add_edge(62, 83, label="fireball_enemy")
G.add_edge(63, 84, label="fireball_enemy")
G.add_edge(64, 85, label="fireball_enemy")
G.add_edge(65, 86, label="fireball_enemy")
G.add_edge(66, 87, label="fireball_enemy")
G.add_edge(67, 88, label="fireball_enemy")
G.add_edge(68, 89, label="fireball_enemy")
G.add_edge(69, 90, label="fireball_enemy")
G.add_edge(70, 91, label="fireball_enemy")
G.add_edge(71, 92, label="fireball_enemy")
G.add_edge(72, 93, label="fireball_enemy")
G.add_edge(73, 94, label="fireball_enemy")

G.add_edge(8, 43,  label="melee_enemy")
G.add_edge(9, 44,  label="melee_enemy")
G.add_edge(10, 45,  label="melee_enemy")
G.add_edge(11, 46, label="melee_enemy")
G.add_edge(12, 47, label="melee_enemy")
G.add_edge(13, 48, label="melee_enemy")
G.add_edge(14, 49, label="melee_enemy")
G.add_edge(15, 50, label="melee_enemy")
G.add_edge(16, 51, label="melee_enemy")
G.add_edge(17, 52, label="melee_enemy")


G.add_edge(1, 95, label="heal_friend")
G.add_edge(2, 96, label="heal_friend")
G.add_edge(3, 97, label="heal_friend")
G.add_edge(4, 98, label="heal_friend")
G.add_edge(5, 99, label="heal_friend")
G.add_edge(6, 100,  label="heal_friend")
G.add_edge(7, 101,label="heal_friend")
G.add_edge(53, 102, label="heal_friend")
G.add_edge(54, 103,  label="heal_friend")
G.add_edge(55, 104,  label="heal_friend")
G.add_edge(56, 105,  label="heal_friend")
G.add_edge(57, 106, label="heal_friend")
G.add_edge(58, 107, label="heal_friend")
G.add_edge(59, 108, label="heal_friend")
G.add_edge(60, 109, label="heal_friend")
G.add_edge(61, 110,  label="heal_friend")
G.add_edge(62, 111, label="heal_friend")
G.add_edge(63, 112,  label="heal_friend")
G.add_edge(64, 113, label="heal_friend")
G.add_edge(65, 114,  label="heal_friend")
G.add_edge(66, 115,  label="heal_friend")
G.add_edge(67, 116,  label="heal_friend")
G.add_edge(68, 117,  label="heal_friend")
G.add_edge(69, 118, label="heal_friend")
G.add_edge(70, 119, label="heal_friend")
G.add_edge(71, 120,  label="heal_friend")
G.add_edge(72, 121,  label="heal_friend")
G.add_edge(73, 122, label="heal_friend")

G.add_edge(95, 123,  label="fireball_enemy")
G.add_edge(96, 124,  label="fireball_enemy")
G.add_edge(97, 125, label="fireball_enemy")
G.add_edge(98, 126,  label="fireball_enemy")
G.add_edge(100, 127,  label="fireball_enemy")
G.add_edge(101, 128,  label="fireball_enemy")
G.add_edge(102, 129,  label="fireball_enemy")
G.add_edge(103, 130,  label="fireball_enemy")
G.add_edge(104, 131, label="fireball_enemy")
G.add_edge(105, 132,  label="fireball_enemy")
G.add_edge(106, 133,  label="fireball_enemy")
G.add_edge(107, 134,  label="fireball_enemy")
G.add_edge(108, 135,  label="fireball_enemy")
G.add_edge(109, 136,  label="fireball_enemy")
G.add_edge(110, 137, label="fireball_enemy")
G.add_edge(111, 138,  label="fireball_enemy")
G.add_edge(112, 139,  label="fireball_enemy")
G.add_edge(113, 140, label="fireball_enemy")
G.add_edge(114, 141,  label="fireball_enemy")
G.add_edge(115, 142,  label="fireball_enemy")
G.add_edge(116, 143, label="fireball_enemy")
G.add_edge(117, 144, label="fireball_enemy")
G.add_edge(118, 145,  label="fireball_enemy")
G.add_edge(119, 146,  label="fireball_enemy")
G.add_edge(120, 147,  label="fireball_enemy")
G.add_edge(121, 148,  label="fireball_enemy")
G.add_edge(122, 149, label="fireball_enemy")

# # Retrieve Node Labels
# node_labels = {node: ", ".join(data["labels"]) for node, data in G.nodes(data=True)}
# for node, labels in node_labels.items():
#     print(f"{node}: {labels}")
# # Retrieve Edge Labels
# for u, v, data in G.edges(data=True):
#     edge_label = data["label"]
#     print(f"Edge ({u}, {v}) has label: {edge_label}")

# plot
# pos = nx.spring_layout(G, seed=3)  # spring_layout
# pos = nx.spectral_layout(G)

# draw
pos = nx.random_layout(G)
nx.draw(G, pos, with_labels=None, node_size=50, node_color="skyblue", font_size=8, font_color="black",
        font_weight="bold", arrowsize=20)
plt.show()
print(G)


# initialization
label_centrality = {}

# Calculate edge centrality and accumulate the centrality of edges with the same label into the dictionary
betweenness_edge_centrality = nx.edge_betweenness_centrality(G, weight='weight')
for (u, v), centrality in betweenness_edge_centrality.items():
    edge_label = G[u][v].get("label", "No Label")
    label_centrality[edge_label] = label_centrality.get(edge_label, 0) + centrality

# Output the total edge-mediated centrality of each label
for label, centrality in label_centrality.items():
    print(f"Label '{label}': Total Betweenness Edge Centrality = {centrality}")





