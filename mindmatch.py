import tkinter as tk
from tkinter import ttk
from breezypythongui import EasyFrame
from tkinter import PhotoImage, Menu, StringVar, Radiobutton, Canvas, Scrollbar

# Therapist data
therapists = [
    {"name": "Dr. John Smith", "specialty": "Anxiety", "gender": "Male", "address": "123 Main St", "phone": "555-123-4567"},
    {"name": "Dr. Sarah Lee", "specialty": "Anxiety", "gender": "Female", "address": "456 Elm St", "phone": "555-987-6543"},
    {"name": "Dr. Mark Green", "specialty": "Depression", "gender": "Male", "address": "789 Oak St", "phone": "555-456-7890"},
    {"name": "Dr. Emily White", "specialty": "Depression", "gender": "Female", "address": "101 Pine St", "phone": "555-654-3210"},
    {"name": "Dr. James Miller", "specialty": "PTSD", "gender": "Male", "address": "202 Birch St", "phone": "555-111-2222"},
    {"name": "Dr. Amanda Brown", "specialty": "Substance Abuse", "gender": "Female", "address": "303 Cedar St", "phone": "555-333-4444"},
    {"name": "Dr. Robert Brown", "specialty": "Stress", "gender": "Male", "address": "404 Maple St", "phone": "555-555-6666"},
    {"name": "Dr. Linda Black", "specialty": "Anxiety", "gender": "Female", "address": "789 Maple St", "phone": "555-888-9999"},
    {"name": "Dr. George White", "specialty": "Anxiety", "gender": "Male", "address": "321 Cherry St", "phone": "555-444-8888"},
    {"name": "Dr. Patricia Young", "specialty": "Anxiety", "gender": "Non-binary", "address": "654 Cypress St", "phone": "555-222-7777"},
]

# Global variable to save selected therapists
saved_therapists = []

class MindMatchApp(EasyFrame):
    def __init__(self):
        super().__init__(title="MindMatch", width=800, height=600, background="#e6e6fa")
        self.gender_var = StringVar(value="Any")
        self.specialty_var = None

        # Load therapist icons and images
        self.load_images()

        # Create the main screen
        self.create_main_screen()

    def load_images(self):
        """Loads images after the root window is created."""
        try:
            self.male_icon = PhotoImage(file="male_icon.gif").subsample(3, 3)
            self.female_icon = PhotoImage(file="female_icon.gif").subsample(3, 3)
            self.any_icon = PhotoImage(file="any.gif").subsample(3, 3)
            self.male_image = PhotoImage(file="male.gif").subsample(3, 3)
            self.female_image = PhotoImage(file="woman.gif").subsample(3, 3)
        except Exception as e:
            print(f"Error loading image: {e}")

    def create_main_screen(self):
        """Main screen with Find a Therapist button."""
        self.clear_screen()
        self.addLabel(text="Welcome to MindMatch", row=0, column=0, columnspan=4, sticky="NSEW", font=("Arial", 20), background="#e6e6fa")

        find_button = tk.Button(self, text="Find a Therapist", command=self.show_gender_specialty_screen, font=("Arial", 14))
        find_button.grid(row=1, column=0, columnspan=4, pady=10)

        self.create_hamburger_menu()

    def show_gender_specialty_screen(self):
        """Combined screen for selecting gender and specialty."""
        self.clear_screen()

        # Scrollable frame setup
        canvas = Canvas(self, width=780, height=560, background="#e6e6fa")
        scroll_y = Scrollbar(self, orient="vertical", command=canvas.yview)

        frame = ttk.Frame(canvas)
        frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scroll_y.set)

        canvas.grid(row=0, column=0, sticky="NSEW", columnspan=4)
        scroll_y.grid(row=0, column=4, sticky="NS")

        # Gender selection
        tk.Label(frame, text="Select Gender", font=("Arial", 16), background="#e6e6fa").grid(row=0, column=0, columnspan=3, pady=10)

        # Add gender icons and radio buttons
        if self.male_icon and self.female_icon and self.any_icon:
            tk.Label(frame, image=self.male_icon, background="#e6e6fa").grid(row=1, column=0, padx=10, pady=5)
            Radiobutton(frame, text="Male", variable=self.gender_var, value="Male", background="#e6e6fa", font=("Arial", 12)).grid(row=2, column=0, padx=10)

            tk.Label(frame, image=self.female_icon, background="#e6e6fa").grid(row=1, column=1, padx=10, pady=5)
            Radiobutton(frame, text="Female", variable=self.gender_var, value="Female", background="#e6e6fa", font=("Arial", 12)).grid(row=2, column=1, padx=10)

            tk.Label(frame, image=self.any_icon, background="#e6e6fa").grid(row=1, column=2, padx=10, pady=5)
            Radiobutton(frame, text="Any", variable=self.gender_var, value="Any", background="#e6e6fa", font=("Arial", 12)).grid(row=2, column=2, padx=10)

        # Specialty dropdown
        tk.Label(frame, text="Select Specialty", font=("Arial", 16), background="#e6e6fa").grid(row=0, column=3, pady=10, padx=20)
        specialties = ["Anxiety", "Depression", "PTSD", "Substance Abuse", "Relationship Counseling", "Career Counseling"]
        self.specialty_var = ttk.Combobox(frame, values=specialties, state="readonly")
        self.specialty_var.grid(row=1, column=3, padx=20)
        self.specialty_var.set("Anxiety")

        # Add a "Next" button explicitly positioned to the right of the specialty dropdown
        next_button = tk.Button(
            frame,
            text="Next",
            command=lambda: self.show_results_screen(self.gender_var.get(), self.specialty_var.get()),
            font=("Arial", 14)
        )
        next_button.grid(row=1, column=4, padx=20)

        self.create_hamburger_menu(back_command=self.create_main_screen)

    def show_results_screen(self, gender, specialty):
        """Displays therapists based on gender and specialty selection."""
        self.clear_screen()

        # Scrollable frame for results
        canvas = Canvas(self, width=780, height=560, background="#e6e6fa")
        scroll_y = Scrollbar(self, orient="vertical", command=canvas.yview)

        frame = ttk.Frame(canvas)
        frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scroll_y.set)

        canvas.grid(row=0, column=0, sticky="NSEW", columnspan=4)
        scroll_y.grid(row=0, column=4, sticky="NS")

        # Filter therapists
        results = [t for t in therapists if (t["gender"] == gender or gender == "Any") and t["specialty"] == specialty]

        tk.Label(frame, text="Therapists", font=("Arial", 16), background="#e6e6fa").grid(row=0, column=0, columnspan=3, pady=10)

        if not results:
            tk.Label(frame, text="No therapists found.", font=("Arial", 14), background="#e6e6fa").grid(row=1, column=0, columnspan=3)
        else:
            for idx, therapist in enumerate(results):
                row = idx + 1
                img = self.male_image if therapist["gender"] == "Male" else self.female_image
                if img:
                    tk.Label(frame, image=img, background="#e6e6fa").grid(row=row, column=0, pady=5, padx=10)
                tk.Label(
                    frame,
                    text=f"{therapist['name']}\n{therapist['address']}\n{therapist['phone']}",
                    font=("Arial", 12),
                    background="#e6e6fa"
                ).grid(row=row, column=1, padx=20)
                tk.Button(
                    frame,
                    text="Save",
                    command=lambda t=therapist: self.save_therapist(t),
                    font=("Arial", 12)
                ).grid(row=row, column=2, padx=20)

        # Add a "Next" button to proceed to the saved therapists screen
        next_button = tk.Button(
            self,
            text="Next",
            command=self.show_saved_therapists_screen,
            font=("Arial", 14)
        )
        next_button.grid(row=1, column=4, padx=20, pady=10)

        self.create_hamburger_menu(back_command=lambda: self.show_gender_specialty_screen())

    def show_saved_therapists_screen(self):
        """Displays saved therapists."""
        self.clear_screen()

        # Scrollable frame for saved therapists
        canvas = Canvas(self, width=780, height=560, background="#e6e6fa")
        scroll_y = Scrollbar(self, orient="vertical", command=canvas.yview)

        frame = ttk.Frame(canvas)
        frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scroll_y.set)

        canvas.grid(row=0, column=0, sticky="NSEW", columnspan=4)
        scroll_y.grid(row=0, column=4, sticky="NS")

        tk.Label(frame, text="Saved Therapists", font=("Arial", 16), background="#e6e6fa").grid(row=0, column=0, columnspan=3, pady=10)

        if not saved_therapists:
            tk.Label(frame, text="No therapists saved yet.", font=("Arial", 14), background="#e6e6fa").grid(row=1, column=0, columnspan=3)
        else:
            for idx, therapist in enumerate(saved_therapists):
                row = idx + 1
                img = self.male_image if therapist["gender"] == "Male" else self.female_image
                if img:
                    tk.Label(frame, image=img, background="#e6e6fa").grid(row=row, column=0, pady=5, padx=10)
                tk.Label(
                    frame,
                    text=f"{therapist['name']} - {therapist['phone']}\n{therapist['address']}",
                    font=("Arial", 12),
                    background="#e6e6fa"
                ).grid(row=row, column=1)

        self.create_hamburger_menu(back_command=self.create_main_screen)

    def save_therapist(self, therapist):
        """Saves a therapist."""
        if therapist not in saved_therapists:
            saved_therapists.append(therapist)
            print(f"Saved: {therapist['name']}")

    def create_hamburger_menu(self, back_command=None):
        """Creates a hamburger menu visible on all screens."""
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        main_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="☰", menu=main_menu)

        main_menu.add_command(label="Home", command=self.create_main_screen)
        if back_command:
            main_menu.add_command(label="Back", command=back_command)

    def clear_screen(self):
        """Clears all widgets from the current frame."""
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    MindMatchApp().mainloop()
