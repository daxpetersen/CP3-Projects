from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import shuffle


class DealOrNoDealApp(App):
    def build(self):
        # Randomize the prizes for 26 suitcases
        self.prizes = [
            0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,
            1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000,
            300000, 400000, 500000, 750000, 1000000
        ]
        shuffle(self.prizes)

        self.selected_suitcase = None
        self.offer = None

        # Create the root widget and dynamically add suitcase buttons
        root = BoxLayout()
        self.populate_suitcases()
        return root

    def populate_suitcases(self):
        suitcase_grid = self.root.ids.suitcase_grid
        suitcase_grid.clear_widgets()

        for i in range(26):
            button = Button(
                text=f"Case {i + 1}",
                size_hint_y=None,
                height="50dp",
                on_press=lambda btn, index=i: self.select_suitcase(index)
            )
            suitcase_grid.add_widget(button)

    def select_suitcase(self, index):
        self.selected_suitcase = index
        self.root.ids.instructions_label.text = f"You selected suitcase {index + 1}."
        self.root.ids.message_label.text = "Now, Deal or No Deal?"

    def make_deal(self):
        if self.selected_suitcase is None:
            self._show_popup("Select a suitcase first!")
            return
        self.offer = sum(self.prizes) // len(self.prizes)  # Average as the bank offer
        self._show_popup(f"You accepted the deal! The bank offered ${self.offer}.")
        self.reset_game()

    def no_deal(self):
        if self.selected_suitcase is None:
            self._show_popup("Select a suitcase first!")
            return
        prize = self.prizes[self.selected_suitcase]  # Prize in the selected suitcase
        self._show_popup(f"No Deal! Your suitcase had ${prize}.")
        self.reset_game()

    def _show_popup(self, message):
        popup = Popup(
            title="Game Result",
            content=Label(text=message),
            size_hint=(0.6, 0.4),
        )
        popup.open()

    def reset_game(self):
        shuffle(self.prizes)
        self.selected_suitcase = None
        self.root.ids.instructions_label.text = "Pick a suitcase!"
        self.root.ids.message_label.text = "Make your choice!"
        self.populate_suitcases()


if __name__ == "__main__":
    DealOrNoDealApp().run()
