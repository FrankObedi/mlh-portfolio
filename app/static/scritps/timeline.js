const url = '/api/timeline_post';
const container = document.querySelector('.pane-text')

// Fetch timeline posts 
async function getPosts(){    
    try {
        const response = await fetch(url);
        if(!response.ok){
            throw new Error(`Response status: ${response.status}`)
        }

        const data = await response.json();

        // check if we got any timeline posts at all
        if(data['timeline_posts'].length == 0){

            // create element to show that no posts were found
            const noPostElement = document.createElement('div')
            noPostElement.classList.add('no-posts-found')

            const noPostMessageElement = document.createElement('h2')
            noPostMessageElement.textContent = "No posts yet. You can start one using the form. 😊"

            noPostElement.appendChild(noPostMessageElement)
            container.appendChild(noPostElement)

        }
        data['timeline_posts'].forEach((post) => {
            createPostElement(post, 'GET')
        })
    }catch(error){
        console.error(error.message)
    }
}

// Call method to fetch all timeline posts on when load
getPosts()

function createPostElement(data, method){

    // remove the no posts found message if there is one
    const noPostElement = document.querySelector('.no-posts-found')
    if(noPostElement !== null){
        container.removeChild(noPostElement)
    }

    // Create a div element for the post
    const postElement = document.createElement('div')
    postElement.classList.add('timeline-post')

    // Create div element for post's user info
    const userElement = document.createElement('div')
    userElement.classList.add('user-info')

    // Create paragraph element that has user's name
    const nameElement = document.createElement('p')
    nameElement.textContent = `${data.name} - ${data.email}`
    nameElement.classList.add('post-user-info')

    // Create paragraph element that has post content
    const contentElement = document.createElement('p')
    contentElement.textContent = `${data.content}`
    contentElement.classList.add('post-content')

    // Create paragraph element that has post date
    const dateElement = document.createElement('p')
    dateElement.textContent = `${data.created_at}`
    dateElement.classList.add('post-date')

    // Add all the post elements to the post div element
    userElement.appendChild(nameElement)
    // userElement.appendChild(emailElement)
    postElement.appendChild(userElement)
    postElement.appendChild(contentElement)
    postElement.appendChild(dateElement)

    // Add the post div element to the container that has all posts
    if(method == 'POST'){
        container.insertBefore(postElement,container.firstChild)
    }else{
        container.appendChild(postElement)
    }
    
}



async function makePost(payload){
    try{
        const response = await fetch(url, {
            method: 'POST',
            body: payload
        })

        if(!response.ok){
            throw new Error(`Response status: ${response.status}`)
        }

        const data = await response.json();        
        // display the new post in the site
        createPostElement(data, 'POST')       
    }
    catch(error){
        console.error(error.message)
    }
}

// handle form submit
form.addEventListener('submit', function(e){
    e.preventDefault()

    // Create payload as new FormData object
    const payload = new FormData(form)
    console.log([payload]) 

    // submit the form to the server
    makePost(payload)
})

    
