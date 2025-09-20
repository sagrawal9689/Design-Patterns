from abc import ABC, abstractmethod

# ----- STATE INTERFACE -----
class State(ABC):
    def __init__(self, player):
        self.player = player  # keep reference to context

    @abstractmethod
    def handle(self):
        pass


# ----- CONCRETE STATES -----
class PlayingState(State):
    def handle(self):
        print("Playing music...")
        self.player.set_state(PausedState(self.player))


class PausedState(State):
    def handle(self):
        print("Music paused.")
        self.player.set_state(StoppedState(self.player))


class StoppedState(State):
    def handle(self):
        print("Music stopped.")
        self.player.set_state(PlayingState(self.player))


# ----- CONTEXT -----
class MediaPlayer:
    def __init__(self):
        self._state = StoppedState(self)

    def set_state(self, state: State):
        self._state = state

    def press_button(self):
        self._state.handle()


# ----- CLIENT -----
if __name__ == "__main__":
    player = MediaPlayer()

    player.press_button()  # Stopped → Playing
    player.press_button()  # Playing → Paused
    player.press_button()  # Paused → Stopped
    player.press_button()  # Stopped → Playing
