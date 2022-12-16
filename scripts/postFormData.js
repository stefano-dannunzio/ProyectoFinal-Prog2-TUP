const loginForm = document.getElementById("login-form");
loginForm.addEventListener("submit", handleFormSubmit);

async function handleFormSubmit(event) {
	/**
	 * Prevenir el comportamiento por defecto del navegador al hacer un submit
	 * asi podemos nosotros manejar los datos.
	 */
	event.preventDefault();
	const form = event.currentTarget;
	const url = form.action;

	try {
		/**
		 * Toma todos los campos del formulario y hace sus valores
		 * disponibles a través de una instacia de `FormData`.
		 * 
		 * @see https://developer.mozilla.org/en-US/docs/Web/API/FormData
		 */
		const formData = new FormData(form);

		/**
		 * Definiremos la función `postFormDataAsJson()` en el próximo paso.
		 */
		const responseData = await postFormDataAsJson({ url, formData });

		/**
		 * Normally you'd want to do something with the response data,
		 * but for this example we'll just log it to the console.
		 */
		console.log({ responseData });

	} catch (error) {
		console.error(error);
	}
}