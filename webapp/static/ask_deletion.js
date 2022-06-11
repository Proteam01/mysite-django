function deleteBeer(beerId) {
    let conf = window.confirm('Do you want to delete this wonderful beer?');
    if (conf) {
        window.location.href=`delete_beer/${beerId}`
    }
}