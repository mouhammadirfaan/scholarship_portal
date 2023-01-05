const unreadMessages = document.querySelectorAll(".unread");
const unread = document.getElementById("notifes");
const markAll = document.getElementById("mark_all");
unread.innerText=unreadMessages.length

unreadMessages.forEach((message) => {
    message.addEventListener("click", () => {
        message.classList.remove("unread");
        const newUnreadMessages = document.querySelectorAll(".unread");
        unread.innerText = newUnreadMessages.length;
    })
})
markAll.addEventListener("click", () => {
    unreadMessages.forEach(message => message.classList.remove("unread"))
    const newUnreadMessages = document.querySelectorAll(".unread");
    unread.innerText = newUnreadMessages.length;
})
// =================================
// =================================
// let input=document.querySelector('input');
// let span = document.querySelector('span');

// input.addEventListener('change', () => {
//     let files = input.files;
//     if(files.length > 0) {
//         if(files[0].size > 10 * 1024){
//             span.innerText = 'File Size Exceeds 10kb';
//             return;
//         }
//     }
//     span.innerTextn = ''
// });