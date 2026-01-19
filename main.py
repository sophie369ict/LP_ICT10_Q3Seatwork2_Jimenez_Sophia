from pyscript import document


#Function runs when the Sign Up button is clicked
def check_team(event=None):

    #For online registration
    registration = document.querySelector('input[name="registration"]:checked')

    #For medical clearance
    medical = document.querySelector('input[name="medical"]:checked')

    #Get selected section from the dropdown
    sections = document.getElementById("sections").value


    # Matches each section to its team logo
    team_logos = {
        "sapphire": "bluebears.png",
        "emerald": "greenhornets.png",
        "ruby": "redbulldogs.png",
        "topaz": "yellowtigers.png"
    }

    # Get the image element where the team logo will be displayed
    logo_el = document.getElementById("team-logo")


    # Check if the student answered both registration and medical questions
    if not registration or not medical:
        document.getElementById("result").innerHTML = "Please answer all questions."
        logo_el.style.display = "none"
        return


    # Get the actual values (yes or no) from the selected radio buttons
    registration = registration.value
    medical = medical.value


    # If the student is registered, medically cleared, and from Sapphire
    if registration == "yes" and medical == "yes" and sections == "sapphire":
        document.getElementById("result").innerHTML = (
            "Congratulations! You are a part of the Blue Bears."
        )
        logo_el.src = team_logos["sapphire"]
        logo_el.style.display = "block"

    # If the student is registered, medically cleared, and from Emerald
    elif registration == "yes" and medical == "yes" and sections == "emerald":
        document.getElementById("result").innerHTML = (
            "Congratulations! You are a part of the Green Hornets."
        )
        logo_el.src = team_logos["emerald"]
        logo_el.style.display = "block"

    # If the student is registered, medically cleared, and from Ruby
    elif registration == "yes" and medical == "yes" and sections == "ruby":
        document.getElementById("result").innerHTML = (
            "Congratulations! You are a part of the Red Bulldogs."
        )
        logo_el.src = team_logos["ruby"]
        logo_el.style.display = "block"

    # If the student is registered, medically cleared, and from Topaz
    elif registration == "yes" and medical == "yes" and sections == "topaz":
        document.getElementById("result").innerHTML = (
            "Congratulations! You are a part of the Yellow Tigers."
        )
        logo_el.src = team_logos["topaz"]
        logo_el.style.display = "block"

    # If the student does not meet the eligibility requirements
    else:
        document.getElementById("result").innerHTML = (
            "Please email the official OBMC address to secure a slot, "
            "or contact the OBMC clinic to submit your medical clearance."
        )
        logo_el.style.display = "none"
