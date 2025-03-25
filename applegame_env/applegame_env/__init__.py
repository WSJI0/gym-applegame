from gymnasium.envs.registration import register

register(
    id="AppleGame-v0",
    entry_point="applegame.env:AppleGameEnv"
)
