 

export const useFeedbackStore = defineStore('feedbackStore', {
    state: () => ({
        
    }),
    actions: {
        async sendFeedback(name, email, message) {
            await useMyFetch('/api/feedback/', {
                method: "post",
                body: {
                    name: name,
                    email: email,
                    message: message
                },
            })
        }
    }
})