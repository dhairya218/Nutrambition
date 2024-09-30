function displayExerciseDetails(exercise) {
  // $('head').append('{% load static %}');

  const exerciseContainer = document.getElementById("exercise-container");
  exerciseContainer.innerHTML = "";

  const heroContainer = document.createElement("div");
  heroContainer.classList.add("hero-container");

  const exerciseGif = document.createElement("div");
  exerciseGif.classList.add("exercise-gif");

  const gifElement = document.createElement("img");
  gifElement.src = exercise.gifUrl;
  gifElement.alt = exercise.name;
  exerciseGif.appendChild(gifElement);

  heroContainer.appendChild(exerciseGif);

  const exerciseInfo = document.createElement("div");
  exerciseInfo.classList.add("exercise-Info");

  const exerciseName = document.createElement("h2");
  exerciseName.textContent = exercise.name;
  exerciseInfo.appendChild(exerciseName);

  const exerciseDescription = document.createElement("p");
  exerciseDescription.classList.add("exercise-description");

  const descriptionText = `Exercises keep you strong. "${
    exercise.name
  }" is one of the best exercises to target your ${exercise.target.toLowerCase()}. It will help you improve your mood and gain energy.`;
  exerciseDescription.textContent = descriptionText;
  exerciseInfo.appendChild(exerciseDescription);

  const exerciseDetailsList = document.createElement("ul");
  exerciseDetailsList.innerHTML = `
      <li>
        <img src="http://127.0.0.1:8000/static/images/bodypart.png" alt="Body Part Icon" class="info-logo"/>
        ${exercise.bodyPart}
      </li>
      <li>
        <img src="http://127.0.0.1:8000/static/images/target.png" alt="Target Icon" class="info-logo"/>
        ${exercise.target}
      </li>
      <li>
        <img src="http://127.0.0.1:8000/static/images/equipment.png" alt="Equipment Icon" class="info-logo"/>
        ${exercise.equipment}
      </li>
    `;

  exerciseInfo.appendChild(exerciseDetailsList);
  heroContainer.appendChild(exerciseInfo);

  exerciseContainer.appendChild(heroContainer);
}

async function fetchAndDisplayExercise() {
  try {
    const exercises = await fetchExercises();
    const urlParams = window.location.href;
    console.log(urlParams);
    const exerciseId = urlParams.match(/id=([^&]+)/)[1];
    const exercise = exercises.find((ex) => ex.id === exerciseId);

    if (exercise) {
      displayExerciseDetails(exercise);
    } else {
      // Handle case when exercise is not found
      const exerciseDetailsContainer =
        document.getElementById("exercise-details");
      exerciseDetailsContainer.innerHTML = "<p>Exercise not found.</p>";
    }
  } catch (error) {
    const exerciseDetailsContainer =
      document.getElementById("exercise-details");
    exerciseDetailsContainer.innerHTML =
      "<p>Failed to fetch exercise details.</p>";
    console.error("Error fetching exercise details:", error);
  }
}

// Calling the fetchAndDisplayExercise function when the page is loaded
document.addEventListener("DOMContentLoaded", fetchAndDisplayExercise);